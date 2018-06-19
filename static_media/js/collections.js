var o_collections = {
    /**
     *
     *  managing collections communication between server and client and
     *  all interaction on the collections tab
     *
     *  for the visual interaction on the browse table/gallery view when adding/removing
     *  from cart see browse.js
     *
     **/
     collectionBehaviors: function() {

        // collection details hide/show
         $('#collection').on("click", '#collection_summary_more', function() {
             if (opus.colls_options_viz) {
                 opus.colls_options_viz=false;
                 $('#collection_summary_more','#collection').text('show options');
                 $('#collection_summary','#collection').animate({height:'8em'});
             } else {
                 opus.colls_options_viz=true;
                 $('#collection_summary_more','#collection').text('hide options');
                 $('#collection_summary','#collection').animate({height:'33em'});
             }
             return false;
         });

         // check an input on selected products and images updates file_info
         $('#collection').on("click",'#download_options input', function() {
             var add_to_url = o_collections.getDownloadFiltersChecked();
             var url = "/opus/collections/download/info/?" + add_to_url
             $.ajax({ url: url + '&fmt=json',
                success: function(json){
                    $('#total_files').fadeOut().html(json['count']).fadeIn();
                    $('#download_size').fadeOut().html(json['size']).fadeIn();
                }});

         });

         // Download Zipped Archive button - click create download zip file link on collections page
         $('#collection').on("click", '#download_csv', function() {
            $(this).attr("href", '/opus/collections/data.csv?'+ o_hash.getHash());
         });

         // Download Zipped Archive button - click create download zip file link on collections page
         $('#collection').on("click", '#collections_summary a#create_zip_file button', function() {
                $('.spinner', "#collections_summary").fadeIn();
                opus.download_in_process = true;
                var add_to_url = o_collections.getDownloadFiltersChecked();
                var url = '/opus/collections/download/default.zip?' + add_to_url + "&" + o_hash.getHash();
                $.ajax({ url: url,
                    success: function(filename){
                        opus.download_in_process = false;
                        if (filename) {
                            $('<li><a href = "' + filename + '">' + filename + '</a></li>').hide().prependTo('ul.zipped_files', "#collections_summary").slideDown('slow');
                            $('.spinner', "#collections_summary").fadeOut();
                        } else {
                            $('<li>No Files Found</li>').hide().prependTo('ul.zipped_files', "#collections_summary").slideDown('fast');
                        }

                    },
                    error: function(e) {

                        $('.spinner', "#collections_summary").fadeOut();
                        $('<li>No Files Found</li>').hide().prependTo('ul.zipped_files', "#collections_summary").slideDown('fast');
                        opus.download_in_process = false;
                    }

                });
                return false;
         });

         // click create zip file link on detail page
         $("#detail").on("click", '#create_zip_file', function() {
             $('#zip_file', "#detail").html(opus.spinner + " zipping files");
              $.ajax({ url: $(this).attr("href"),
                     success: function(json){
                         $('#zip_file').html('<a href = "' + json + '">' + json + '</a>');
                     }});
              return false;
         });

         // empty collection button
         $('#collection').on("click", '#empty_collection', function() {
             if (confirm("are you sure you want to delete all observations in your collection?")) {
                 o_collections.emptyCollection();
               }
             return false;
         });
     },

     // download filters
     getDownloadFiltersChecked: function() {
         // returned as url string
         var product_types = [];
         var image_types = [];
         var add_to_url = [];
         $('ul#product_types input:checkbox:checked').each(function(){
               product_types.push($(this).val());
             });
         if (product_types.length) {}
         $('ul#image_types input:checkbox:checked').each(function(){
               image_types.push($(this).val());
             });
        var checked_filters = {"types":product_types, "previews":image_types };

        for (var filter_name in checked_filters) {
          if (checked_filters[filter_name].length) {
              add_to_url.push(filter_name + "=" + checked_filters[filter_name].join(','));
          }
        }
        return add_to_url.join('&');
     },

    // init an existing collection on page load
    initCollection: function() {
        // returns any user collection saved in session
        $.ajax({ url: "/opus/collections/default/status.json",
            dataType:"json",
            success: function(data){
                   var count = data['count'];
                   if (parseInt(count, 10)) {
                       opus.collection_change = true;

                       opus.mainTabDisplay('collection');  // make sure the main site tab label is displayed

                       $('#collection_tab').fadeIn();
                       opus.colls_pages = Math.ceil(count/opus.prefs.limit);
                       $('#collection_count').html(count);
                   }
                   opus.lastCartRequestNo = parseInt(data['expected_request_no']) - 1
            }});
    },

    // get Collections tab
    getCollectionsTab: function() {
        clearInterval(opus.scroll_watch_interval); // hold on cowgirl only 1 page at a time

        if (opus.collection_change) {
            var zipped_files_html = $('.zipped_files', '#collection').html();

            $('.collection_details', '#collection').html(opus.spinner);

            // reset page no
            opus.last_page_drawn['colls_gallery'] = 0;
            opus.last_page_drawn['colls_data'] = 0;

            // redux: speed this up by splitting into 2 ajax calls

            // redux: draw the template immediately after this or only empty individual elements
            $('.gallery ul.ace-thumbnails', '#collection').empty();
            $('.data', '#collection').empty();

            /*
            // redux: first get the product counts
            $.ajax({ url: "/opus/collections/default/product_counts.html",
                   success: function(html){

                        // then get a page of images + metadata
                        $.ajax({ url: "/opus/collections/default/thumbnails.html",
                               success: function(html){},
                               error: function(html){}
                           });

                   },
                   error: function(html){}
               });
            */

            // redux: and nix this big thing:
            $.ajax({ url: "/opus/collections/default/view.html",
                success: function(html){
                    // this div lives in the in the nav menu template
                    $('.collection_details', '#collection').hide().html(html).fadeIn();

                    opus.collection_change = false;
                    if (opus.download_in_process) {
                        $('.spinner', "#collections_summary").fadeIn();
                    }

                    $('#colls_pages').html(opus.colls_pages);

                    o_browse.getBrowseTab();

                    if (zipped_files_html) {
                        $('.zipped_files', '#collection').html(zipped_files_html);
                    }

                }});
        }
    },

    // when you add to a collection you are really adding to a queue, this processes that queue
    processCollectionQueue: function() {
        // start the lowest item in the queue, then trigger sendCollectionRequest again?
        var found = false;
        for (var request_no in opus.collection_queue) {
            if (!opus.collection_queue[request_no]['sent']) {
                found = true;
                // this request is waiting to be sent
                var action = opus.collection_queue[request_no]['action'];
                var opus_id = opus.collection_queue[request_no]['opus_id'];
                // alert('calling sendCollectionRequest for ' + opus_id);
                o_collections.sendCollectionRequest(action,opus_id,request_no);
            }
        }
        if (!found) {
            // queue is empty quit lookin' at it
            o_collections.resetCollectionQueue();
        }
    },

    // action = add/remove/addrange/removerange/addall
    sendCollectionRequest: function(action,opus_id,request_no) {
        // this sends the ajax call to edit the cart on the server
        // but this should really be a private method
        // for adding/removing from cart see edit_collection()

        if (!opus.collection_q_intrvl) {
            opus.collection_q_intrvl = setInterval("o_collections.processCollectionQueue()", 500); // resends any stray requests not recvd back from server
        }

        var url = "/opus/collections/default/" + action + ".json?request=" + request_no
        switch (action) {
            case "add":
            case "remove":
            case "removerange":
                url += "&opus_id=" + opus_id;
                break;

            case "addrange":
                url += "&add_range=" + opus_id;
                // need to send to server what page this range lands and what limit of that page is
                // limit should include all observations showing on page
                // must adjust limit + page to account for total number of results showing on page

                // server uses offset = (page_no-1)*limit
                // i.e. the offset of the 23rd page at 100 per page starts with the 2200st record:

                // first find what does opus.prefs.page say we are looking at:
                var view_info = o_browse.getViewInfo();
                var namespace = view_info['namespace']; // either '#collection' or '#browse'
                var prefix = view_info['prefix'];       // either 'colls_' or ''
                var view_var = opus.prefs[prefix + 'browse'];  // either 'gallery' or 'data'

                var first_page = o_browse.getCurrentPage();
                var last_page = opus.last_page_drawn[prefix + view_var];

                // now find the number of results showing on the page, different from opus.prefs.limit:
                // number of "pages" showing on screen at any time = limit * (1+footer_clicks)
                // i.e., you've got 100 on screen, you click footer 4 times, now you've got 500 showing
                // multiply that by 2 because our results may span no more than 2 "pages" at our new limit on the server
                var limit = opus.prefs.limit * (last_page - first_page + 1);

                // server says offset = (page_no-1)*limit
                // solve that equation for page our new page value:
                url += '&' + o_hash.getHash();

                // update the page and limit in url
                var url_split = url.split('&');
                for (var key in url_split) {
                    var param = url_split[key].split('=')[0];
                    if (param == 'page') {
                        delete url_split[key];
                    }
                    if (param == 'limit') {
                        delete url_split[key];
                    }
                }
                url = url_split.join('&');
                url = url + "&limit=" + limit + "&page=" + first_page;
                break;

          case "addall":
              // currently not implemented
              url += '&' + o_hash.getHash();
              break;
        }

        $.ajax({
            url: url,
            dataType: "json",
            success: function(data) {
                if (data['err'] == undefined) {
                    opus.collection_queue[request_no]['sent'] = true; // server has recvd this request
                    var server_latest_processed = data['request_no'];
                    if (server_latest_processed == opus.lastCartRequestNo) {
                        // server has process all collection requests, this count is valid
                        var count = data['count'];
                        $('#collection_count').html(count);
                        opus.colls_pages = Math.ceil(count/opus.prefs.limit);
                        o_collections.resetCollectionQueue();
                    } else {
                           // // alert('server last ' + server_latest_processed + ' client: ' + opus.lastCartRequestNo)
                    }
                } else {
                  // post error where...?
                }
            },
            error: function() {
                //$('#notification-bar').text('An error occurred');
            }
        });
    },

    emptyCollection: function() {
        // remove all
        o_collections.resetCollectionQueue();
        opus.lastCartRequestNo = 0;

        // change indicator to zero and let the server know:
        $.ajax({ url: "/opus/collections/reset.html",
            success: function(html){
                $('#collection_count').html('0');
                opus.colls_pages = 0;
            }, error: function(e) {
            }
        });

        // hide the collection data viewing page
        function collTransition() {
            $('.gallery, .data_table', '#collection').fadeOut(function() {
                $('.gallery ul.ace-thumbnails, .data_table ul','#collection').empty();
            });
            $('.gallery, .data_table','#collection').fadeIn();
        }
        collTransition();

        // remove 'in collection' styles in gallery/data view
        $('.tools-bottom', '.gallery').removeClass("in"); // this class keeps parent visible when mouseout
        $( ".tools-bottom a", '.gallery').find('i').removeClass('thumb_selected_icon');
        $('.thumb_overlay', '.gallery').removeClass('thumb_selected');
        $('.data_checkbox', '.data_table').removeClass('fa-check-square-o').addClass('fa-square-o');
    },

    resetCollectionQueue: function() {
        clearInterval(opus.collection_q_intrvl);
        opus.collection_queue = [];
    },

    editCollection: function(opus_id, action) {
        opus.mainTabDisplay('collection');  // make sure the main site tab label is displayed

        opus.collection_change = true;
        opus.lastCartRequestNo++;
        // $('.collections_extra').html(opus.spinner);
        // $('#collection_tab').fadeIn();
        opus.collection_queue[opus.lastCartRequestNo] = {"action":action, "opus_id":opus_id, "sent":false};

        o_collections.processCollectionQueue();
    },


};
