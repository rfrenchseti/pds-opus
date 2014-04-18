var o_search = {

    /**
     *
     *  Everything that appears on the search tab
     *
     **/

    searchBehaviors: function() {

        /** this is handled by cookie now in o_widgets.getWidget()
        // restart button preserves widget arrangement
        $('#restart>a').live("click", function() {
            hash = [];
            if (opus.prefs.widgets.length || opus.prefs.widgets2.length) {

                if (opus.prefs.widgets.length) hash[hash.length] = "widgets=" + opus.prefs.widgets.join(',');
                if (opus.prefs.widgets2.length) hash[hash.length] = 'widgets2=' + opus.prefs.widgets2.join(',');
            }
            // $(this).attr("href",'/#/' + hash.join('&'));
            $('.formscolumn').html('');
            $('#formscolumn1').html(opus.spinner);
            window.location.hash =  '/' + hash.join('&');
            window.location.reload(true);
            return false;

        });
        **/

        $('#result_count').parent().hover(
            function(){ $('#result_count').addClass('result_count_hover'); },
            function(){ $('#result_count').removeClass('result_count_hover'); }
        )

        // the split form buttons - view the search form in 1 or 2 columns
        $('#split_search_form a').live('click', function() {
            col = $(this).attr("href");
            if (col == '#2col') {
                // clicked '2 columns' so add a 2nd column
                if (opus.search_form_cols==1) o_widgets.resetWidgetScrolls(); // changing shap calls for reset scrolls
                opus.search_form_cols = 2;
                o_search.addSecondFormsCol();
            } else {
                // clicked '1 column' remove the 2nd column
                if (opus.search_form_cols==2) o_widgets.resetWidgetScrolls(); // reset all scroll positions
                // first move the widgets to the first column
                opus.search_form_cols = 1;
                $('#formscolumn1').width('78%');
                $('#formscolumn2 .widget').each(function() {
                    $(this).appendTo('#formscolumn1');
                    slug = $(this).attr('id').split('__')[1];
                    opus.prefs.widgets.push(slug);
                    opus.prefs.widgets2.splice(jQuery.inArray(slug,opus.prefs.widgets2),1);
                    o_hash.updateHash();
                });

                $('#formscolumn1 .widget').each(function() {
                    o_widgets.adjustWidgetWidth(this);
                });
                // remove the 2nd column, widen the first column
                $('#formscolumn2').remove();
            }

            o_widgets.updateWidgetCookies();
            return false;
        });

        // range behaviors and string behaviors for search widgets - input box
        $('.RANGE input, .STRING input','#search').live('change', function() {

            opus.user_clicked=true;
            slug = $(this).attr("name");
            css_class = $(this).attr("class").split(' ')[0]; // class will be STRING, min or max

            // get values of all inputs
            var values = [];
            if (css_class == 'STRING') {
                $('#widget__' + slug + ' .widget_inner input').each(function() {
                    values[values.length] = $(this).val();
                });
                opus.selections[slug] = values;

            } else {
                // range query
                var slug_no_num = slug.match(/(.*)[1|2]/)[1];
                // min
                $('#widget__' + slug_no_num + '1 input.min', '#search').each(function() {
                    values[values.length] = $(this).val();
                });
                opus.selections[slug_no_num + '1'] = values;
                // max
                values = [];
                $('#widget__' + slug_no_num + '1 input.max', '#search').each(function() {
                    values[values.length] = $(this).val();
                });
                opus.selections[slug_no_num + '2'] = values;
            }
            o_hash.updateHash();
        });

        // range behaviors and string behaviors for search widgets - qtype select dropdown
        $('select','#search').live('change',function() {
            opus.user_clicked=true;
            var qtypes = [];
            var form_type = $(this).parent().parent().parent().parent().attr("class").split(' ')[1];


            if (form_type == 'RANGE') {
                slug_no_num = $(this).attr("name").match(/-(.*)/)[1];
                slug = slug_no_num + '1';



                $('#widget__' + slug + ' select').each(function() {
                    qtypes[qtypes.length] = $(this).val();
                });
                opus.extras['qtype-' + slug_no_num] = qtypes;

            } else if (form_type == 'STRING') {
                slug = $(this).attr("name").match(/-(.*)/)[1];
                $('#widget__' + slug + ' select').each(function() {
                    qtypes[qtypes.length] = $(this).val();
                });
                opus.extras['qtype-' + slug] = qtypes;
            }
            o_hash.updateHash();
        });

        // add range add string search behaviors
        $('.STRING a.add_input, .RANGE a.add_input','#search').live("click", function() {

            slug = $(this).parent().parent().parent().parent().parent().parent().attr("id").match(/\__(.*)/)[1]; // shoot me now.

            count = $('#widget__' + slug + ' input').length + 1;

            // no bring in another note form
            // we don't want
            $.ajax({ url: "/opus/forms/widget/" + slug + '.html?addlink=false',
                success: function(widget_str){
                    // we don't want to insert the entire widget, only the span class = "widget_form" section
                    html = widget_str.match(/<section>([\s\S]*)<\/section>/)[0];
                    $(html).appendTo('#widget__' + slug + ' .widget_inner');
                }});
            return false;

        });

        // add range add string search behaviors - remove string
        $('.STRING a.remove_input, .RANGE a.remove_input','#search').live("click", function() {

            var slug = $(this).parent().parent().parent().parent().parent().parent().attr("id").match(/\__(.*)/)[1];
            form_type = 'STRING';
            if ($('#widget__' + slug + ' .widget_inner').hasClass('RANGE')) form_type = 'RANGE';
            var qname = 'qtype-' + slug;

            if (form_type == 'RANGE') {
                var min = slug.match(/(.*)[1|2]/)[1] + '1';
                var max = slug.match(/(.*)[1|2]/)[1] + '2';
                var input_val_max = $(this).parent().prev().prev().children('input').val();
                var input_val_min = $(this).parent().prev().prev().prev().children('input').val();


                $(this).parent().parent().remove(); // the section

                // removing a range means removing any values entered from the opus.selections and updating the hash
                if (typeof(opus.selections[min]) != 'undefined' || typeof(opus.selections[min])  != 'undefined') {
                    // this range is contrained, are we removing
                    // loop through the opus.selections to find the pair we are removing
                    lngth = Math.max(opus.selections[min].length, opus.selections[max].length);
                    for (var key=0;key<lngth;key++) {
                        if (opus.selections[min][key] == input_val_min && opus.selections[max][key] == input_val_max) {
                            // this is the pair we need to remove
                            opus.selections[min].splice(key,1);
                            opus.selections[max].splice(key,1);
                            if (jQuery.inArray(qname, opus.extras) > -1 && typeof(opus.extras[qname]) != 'undefined') {
                                opus.extras[qname].splice(key,1);
                            }
                            break;
                        }
                    }
                }
            } else { // this is a STRING field
                var input_val = $(this).parent().prev().prev().children('input').val();

                $(this).parent().prev().prev().remove(); // the section
                $(this).parent().prev().remove(); // the section
                $(this).parent().remove(); // the section
                // $(this).parent().prev().remove(); // the section

                if (typeof(opus.selections[slug]) != 'undefined') {
                    for (key in opus.selections[slug]) {
                         if (opus.selections[slug][key] == input_val) {
                             opus.selections[slug].splice(key,1);
                              if (jQuery.inArray(qname, opus.extras) > -1 && typeof(opus.extras[qname]) != 'undefined') {
                                 opus.extras[qname].splice(key,1);
                             }
                             break;
                         }
                    }
                }
            }
                o_hash.updateHash();
                return false;
            });
    },

    getSearchTab: function() {
        // widgets1 is the left column of widgets, wigets2 is the optional right col

        // get any prefs from cookies
        if (!opus.prefs.widgets.length && $.cookie("widgets")) {
            opus.prefs.widgets = $.cookie("widgets").split(',');
        }
        if (!opus.prefs.widgets2.length && $.cookie("widgets2")) {
            opus.prefs.widgets2 = $.cookie("widgets2").split(',');
        }

        // get menu
        o_menu.getMenu();

        // find and place the widgets
        if (!opus.prefs.widgets.length && !opus.prefs.widgets2.length) {
            // no widgets defined, get the default widgets
            opus.prefs.widgets = ['planet','target'];
            o_widgets.placeWidgetContainers();
            o_widgets.getWidget('planet','#formscolumn1');
            o_widgets.getWidget('target','#formscolumn1');
        } else {
            if (!opus.widget_elements_drawn.length) {
                o_widgets.placeWidgetContainers();
            }
        }

        o_widgets.updateWidgetCookies();

        for (key in opus.prefs.widgets) {  // fetch each widget
            slug = opus.prefs.widgets[key];
            if (jQuery.inArray(slug, opus.widgets_drawn) < 0) {  // only draw if not already drawn
                o_widgets.getWidget(slug,'#formscolumn1');
            }
        }
        for (key in jQuery.unique(opus.prefs.widgets2)) {  // fetch each widget
            slug = opus.prefs.widgets2[key];
            if (jQuery.inArray(slug, opus.widgets_drawn) < 0) {  // only draw if not already drawn
      	        o_widgets.getWidget(slug,'#formscolumn2');
      	    }
        }

    },


    addSecondFormsCol: function() {
        var width = '35%';
        if (!$('#formscolumn2').length) {
            $('.formscolumn').width(width);

            $('#formscolumn1').after('<ul  id = "formscolumn2" style = "width:' + width + '" class="formscolumn"></ul>')
                              .animate({width:width},'fast');
            $('#formscolumn1, #formscolumn2').sortable({
                    connectWith: '.formscolumn',
                    handle:'.widget_draghandle',
                    cursor: 'crosshair',
                    stop: function(event,ui) {
                        o_widgets.widgetDrop(ui);
                    }
            });

            $('#formscolumn1 .widget').each(function() {
                o_widgets.adjustWidgetWidth(this);
            });

        }
    },

    getHinting: function(slug) {
        if (slug.match(/.*(1|2)/)) {
            // this is a range field
            o_search.getRangeEndpoints(slug);

        } else {
            // mult field
            o_search.getValidMults(slug);
        }
    },

    getRangeEndpoints: function(slug) {

        $('#widget__' + slug + ' .spinner').addClass('spinning');

        var url = "/opus/api/meta/range/endpoints/" + slug + ".json?" + o_hash.getHash() +  '&reqno=' + opus.lastRequestNo;
            $.ajax({url: url,
                dataType:"json",
                success: function(multdata){

                    $('#widget__' + slug + ' .spinner').removeClass('spinning');

                    if (multdata['reqno'] < opus.lastRequestNo) {
                        return;
                    }

                    min = multdata['min'];
                    max = multdata['max'];
                    nulls = multdata['nulls'];

                    widget = "widget__" + slug;
                    $('#hint__' + slug).html("<span>min: " + min + "</span><span>max: " + max + "</span><span> nulls: " + nulls + '</span>');

                },
                statusCode: {
                    404: function() {
                      $('#widget__' + slug + ' .spinner').removeClass('spinning');
                  }
                },
                error:function (xhr, ajaxOptions, thrownError){
                    $('#widget__' + slug + ' .spinner').removeClass('spinning');
                }
            }); // end mults ajax
    },

    getValidMults: function (slug) {
        // turn on spinner
        if (jQuery.isEmptyObject(o_hash.getSelectionsFromHash())) return;
        $('#widget__' + slug + ' .spinner').addClass('spinning');

        var url = "/opus/api/meta/mults/" + slug + ".json?" + o_hash.getHash() +  '&reqno=' + opus.lastRequestNo;
        $.ajax({url: url,
            dataType:"json",
            success: function(multdata){

                $('#widget__' + slug + ' .spinner').removeClass('spinning');

                if (multdata['reqno'] < opus.lastRequestNo) {
                    return;
                }
                slug = multdata['field'];
                widget = "widget__" + slug;
                mults = multdata['mults'];
                $('#' + widget + ' input').each( function() {
                    value = $(this).attr('value');
                    id = '#hint__' + value.split(' ').join('_'); // id of hinting span
                    if (mults[value]){
                          $(id).html('<span>' + mults[value] + '</span>');
                    } else $(id).html('<span>0</span>');

                });

            },
            statusCode: {
                404: function() {
                  $('#widget__' + slug + ' .spinner').removeClass('spinning');
              }
            },
            error:function (xhr, ajaxOptions, thrownError){
                $('#widget__' + slug + ' .spinner').removeClass('spinning');
            }
        }); // end mults ajax

    },



};

