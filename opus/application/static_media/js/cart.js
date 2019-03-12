var o_cart = {
    lastCartRequestNo: 0,
    lastRequestNo: 0,

    /**
     *
     *  managing cart communication between server and client and
     *  all interaction on the cart tab
     *
     *  for the visual interaction on the browse table/gallery view when adding/removing
     *  from cart see browse.js
     *
     **/

     cartBehaviors: function() {
         // nav bar
         $("#cart").on("click", ".download_csv", function(e) {
             window.open(`/opus/__cart/data.csv?${o_hash.getHash()}`, '_blank');
             //$(this).attr("href", "/opus/__cart/data.csv?"+ o_hash.getHash());
         });

         $("#cart").on("click", ".downloadData", function(e) {
             o_cart.downloadZip("create_zip_data_file", "Internal error creating data zip file");
         });

         $("#cart").on("click", ".downloadURL", function(e) {
             o_cart.downloadZip("create_zip_url_file", "Internal error creating URL zip file");
         });
         $("#cart").on("click", ".metadataModal", function(e) {

         });
         $("#cart").on("click", ".emptyCart", function() {
             if (confirm("Are you sure you want to remove all observations from your cart?")) {
                 o_cart.emptyCart();
             }
         });

         // check an input on selected products and images updates file_info
         $("#cart").on("click","#download_options input", function() {
             let add_to_url = o_cart.getDownloadFiltersChecked();
             o_cart.lastCartRequestNo++;
             let url = "/opus/__cart/status.json?reqno=" + o_cart.lastCartRequestNo + "&" + add_to_url + "&download=1";
             $.getJSON(url, function(info) {
                 if(info.reqno < o_cart.lastCartRequestNo) {
                     return;
                 }
                 $("#total_download_size").fadeOut().html(info.total_download_size_pretty).fadeIn();
             });
         });
     },

     // download filters
     getDownloadFiltersChecked: function() {
         // returned as url string
         let product_types = [];
         let image_types = [];
         let add_to_url = [];
         $("ul#product_types input:checkbox:checked").each(function(){
             product_types.push($(this).val());
         });
         let checked_filters = {"types":product_types};

         for (let filter_name in checked_filters) {
             if (checked_filters[filter_name].length) {
                 add_to_url.push(filter_name + "=" + checked_filters[filter_name].join(','));
             }
        }
        return add_to_url.join('&');
     },

     downloadZip: function(type, errorMsg) {
         if (opus.download_in_process) {
             return false;
         }
         $("#download_links").show();
         opus.download_in_process = true;
         $(".spinner", "#download_links").fadeIn().css("display","inline-block");

         let add_to_url = o_cart.getDownloadFiltersChecked();
         let url = "/opus/__cart/download.json?" + add_to_url + "&" + o_hash.getHash();
         url += (type == "create_zip_url_file" ? "&urlonly=1" : "");
         $.ajax({
             url: url,
             dataType: "json",
             success: function(data){
                 if (data.error !== undefined) {
                     $(`<li>${data.error}</li>`).hide().prependTo("ul.zippedFiles", "#cart_summary").slideDown("fast");
                 } else {
                     $(`<li><a href = "${data.filename}">${data.filename}</a></li>`).hide().prependTo("ul.zippedFiles", "#cart_summary").slideDown("slow");
                 }
                 $(".spinner", "#download_links").fadeOut();
             },
             error: function(e) {
                 $(".spinner", "#download_links").fadeOut();
                 $(`<li>${errorMsg}</li>`).hide().prependTo("ul.zippedFiles", "#cart_summary").slideDown("fast");
             },
             complete: function() {
                 opus.download_in_process = false;
             }
         });
     },

     adjustProductInfoHeight: function() {
         let containerHeight = $(window).height()-120;
         let downloadOptionsContainer = $(window).height()-90;
         let cartSummaryHeight = $("#cart_summary").height();
         $("#cart .sidebar_wrapper").height(downloadOptionsContainer);
         $("#cart .gallery-contents").height(containerHeight);

         // The following steps will hide the y-scrollbar when it's not needed.
         // Without these steps, y-scrollbar will exist at the beginning, and disappear after the first attempt of scrolling
         if(o_cart.downloadOptionsScrollbar) {
             if(downloadOptionsContainer > cartSummaryHeight) {
                 if(!$("#download-options-container .ps__rail-y").hasClass("hide_ps__rail-y")) {
                     $("#download-options-container .ps__rail-y").addClass("hide_ps__rail-y");
                     o_cart.downloadOptionsScrollbar.settings.suppressScrollY = true;
                 }
             } else {
                 $("#download-options-container .ps__rail-y").removeClass("hide_ps__rail-y");
                 o_cart.downloadOptionsScrollbar.settings.suppressScrollY = false;
             }
             o_cart.downloadOptionsScrollbar.update();
         }

         if(o_cart.cartGalleryScrollbar) {
             o_cart.cartGalleryScrollbar.update();
         }
     },

     updateCartStatus: function(status) {
         if (status.reqno < o_cart.lastCartRequestNo) {
             return;
         }
         let count = status.count;
         $("#cart_count").html(count);
         if (status.total_download_size_pretty !== undefined) {
             $("#total_download_size").fadeOut().html(status.total_download_size_pretty).fadeIn();
         }
         o_cart.adjustProductInfoHeight();
     },


     // init an existing cart on page load
     initCart: function() {
        // returns any user cart saved in session
        o_cart.lastCartRequestNo++;
        $.getJSON("/opus/__cart/status.json?reqno=" + o_cart.lastCartRequestNo, function(statusData) {
            if(statusData.reqno < o_cart.lastCartRequestNo) {
                return;
            }
            o_cart.updateCartStatus(statusData);
        });
     },

     loadCartData: function (page) {
        //window.scrollTo(0,opus.browse_view_scrolls[opus.prefs.browse]);
        page = (page == undefined ? 1 : (opus.cart_change ? 1 : page));

        let view = o_browse.getViewInfo();
        let base_url = "/opus/__api/dataimages.json?";
        o_cart.lastRequestNo++;
        let url = o_hash.getHash() + "&reqno=" + o_cart.lastRequestNo + view.add_to_url;

        url = o_browse.updatePageInUrl(url, page);

        // metadata; used for both table and gallery
        $.getJSON(base_url + url, function(data) {
            if (data.reqno < o_cart.lastRequestNo) {
                return;
            }
            if (opus.col_labels.length === 0) {
                opus.col_labels = data.columns;
            }
            o_browse.renderGalleryAndTable(data, this.url);
            o_browse.updateSortOrder(data);

            if (opus.cart_change) {
                // for infinite scroll
                $("#cart .gallery-contents").infiniteScroll({
                    path: o_browse.updatePageInUrl(this.url, "{{#}}"),
                    responseType: "text",
                    status: "#cart .page-load-status",
                    elementScroll: true,
                    history: false,
                    debug: false,
                });
                $("#cart .gallery-contents").on( "load.infiniteScroll", function( event, response, path ) {
                    let jsonData = JSON.parse( response );
                    o_browse.renderGalleryAndTable(jsonData, path);
                });
                opus.cart_change = false;
            }
            o_cart.adjustProductInfoHeight();
        });
    },

    // get Cart tab
    getCartTab: function() {
        o_browse.renderMetadataSelector();   // just do this in background so there's no delay when we want it...
        if (opus.cart_change) {
            var zippedFiles_html = $(".zippedFiles", "#cart").html();

            // don't forget to remove existing stuff before append
            $(".gallery", "#cart").html("");

            $(".cart_details", "#cart").html(opus.spinner);

            // reset page no
            opus.lastPageDrawn.cart = 0;

            // redux: and nix this big thing:
            $.ajax({ url: "/opus/__cart/view.html",
                success: function(html) {
                    // this div lives in the in the nav menu template
                    $(".cart_details", "#cart").hide().html(html).fadeIn();

                    if (opus.download_in_process) {
                        $(".spinner", "#cart_summary").fadeIn();
                    }

                    o_cart.loadCartData();

                    if (zippedFiles_html) {
                        $(".zippedFiles", "#cart").html(zippedFiles_html);
                    }

                    o_cart.downloadOptionsScrollbar = new PerfectScrollbar("#download-options-container");
                    o_cart.cartGalleryScrollbar = new PerfectScrollbar("#cart .gallery-contents", {
                        suppressScrollX: true,
                    });
                    let adjustProductInfoHeight = _.debounce(o_cart.adjustProductInfoHeight, 200);
                    adjustProductInfoHeight();
                }
            });
        } else {
            o_cart.adjustProductInfoHeight();
            return;
        }
    },

    isIn: function(opusId) {
        return  $("[data-id='"+opusId+"'].thumbnail-container").hasClass("in");
    },

    emptyCart: function(returnToSearch=false) {
        // change indicator to zero and let the server know:
        $.getJSON("/opus/__cart/reset.json", function(data) {
            $("#cart_count").html("0");
            opus.cart_change = true;
            $("#cart .navbar").hide();
            $("#cart .sort-order-container").hide();
            if(!returnToSearch){
                opus.changeTab("cart");
            } else {
                opus.changeTab("search");
            }
        });

        let buttonInfo = o_browse.cartButtonInfo("in");
        $(".thumbnail-container.in [data-icon=cart]").html(`<i class="${buttonInfo.icon} fa-xs"></i>`);
        $(".thumbnail-container.in").removeClass("in");
        $("#dataTable input").prop("checked", false);
    },

    toggleInCart: function(fromOpusId, toOpusId) {
        let fromElem = o_browse.getGalleryElement(fromOpusId);

        // handle it as range
        if (toOpusId != undefined) {
            let action = (fromElem.hasClass("in") ? "removerange" : "addrange");
            let cartAction = (action == "addrange");
            let toElem = o_browse.getGalleryElement(toOpusId);
            let fromIndex = $(".thumbnail-container").index(fromElem);
            let toIndex = $(".thumbnail-container").index(toElem);

            // reorder if need be
            if (fromIndex > toIndex) {
                [fromIndex, toIndex] = [toIndex, fromIndex];
            }
            let length = toIndex - fromIndex+1;
            let namespace = o_browse.getViewInfo().namespace;
            let elementArray = $(namespace + " .thumbnail-container");
            let opusIdRange = $(elementArray[fromIndex]).data("id") + ","+ $(elementArray[toIndex]).data("id")
            console.log("end range "+action+" : "+opusIdRange);
            $.each(elementArray.splice(fromIndex, length), function(index, elem) {
                let opusId = $(elem).data("id");
                let status = "in";
                if (action == "addrange") {
                    $(elem).addClass("in");
                    status = "out"; // this is only so that we can make sure the icon is a trash can
                } else {
                    $(elem).removeClass("in");
                }
                $("input[name="+opusId+"]").prop("checked", (action == "addrange"));
                o_browse.updateCartIcon(opusId, status);
            });
            o_cart.editCart(opusIdRange, action);
            o_browse.undoRangeSelect(namespace);
        } else {
            // note - doing it this way handles the obs on the browse tab at the same time
            $(`.thumbnail-container[data-id=${fromOpusId}]`).toggleClass("in");

            let action = (fromElem.hasClass("in") ? "add" : "remove");
            o_browse.updateCartIcon(fromOpusId, action);
            o_cart.editCart(fromOpusId, action);
            return action;
        }
    },

    // action = add/remove/addrange/removerange/addall
    editCart: function(opusId, action) {
        opus.cart_change = true;

        var viewInfo = o_browse.getViewInfo();
        var url = "/opus/__cart/" + action + ".json?";
        switch (action) {
            case "add":
            case "remove":
                url += "opusid=" + opusId;
                break;

            case "removerange":
            case "addrange":
                url += "range=" + opusId;
                // need to send to server what page this range lands and what limit of that page is
                // limit should include all observations showing on page
                // must adjust limit + page to account for total number of results showing on page

                // server uses offset = (page_no-1)*limit
                // i.e. the offset of the 23rd page at 100 per page starts with the 2200st record:

                let first_page = o_browse.getCurrentPage();
                let last_page = opus.lastPageDrawn[opus.prefs.view];

                // now find the number of results showing on the page, different from opus.prefs.limit:
                // number of "pages" showing on screen at any time = limit * (1+footer_clicks)
                // i.e., you've got 100 on screen, you click footer 4 times, now you've got 500 showing
                // multiply that by 2 because our results may span no more than 2 "pages" at our new limit on the server
                let limit = opus.prefs.limit * (last_page - first_page + 1);

                let hashArray = o_hash.getHashArray();
                if (hashArray.page !== undefined)
                    delete hashArray.page;
                if (hashArray.limit !== undefined)
                    delete hashArray.limit;

                url += '&' + o_hash.hashArrayToHashString(hashArray);
                url = url + "&limit=" + limit + "&page=" + first_page;
                break;

          case "addall":
              url += o_hash.getHash();
              break;
        }

        // Minor performance check - if we don't need a total download size, don't bother
        // Only the selection tab is interested in updating that count at this time.
        let add_to_url = "";
        if (opus.prefs.view == "cart") {
            add_to_url = "&download=1&" + o_cart.getDownloadFiltersChecked();
        }

        o_cart.lastCartRequestNo++;
        $.getJSON(url  + add_to_url + "&reqno=" + o_cart.lastCartRequestNo, function(statusData) {
            o_cart.updateCartStatus(statusData);
        });
    },
};