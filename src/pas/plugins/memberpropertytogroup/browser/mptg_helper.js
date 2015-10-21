jQuery('head').append( jQuery('<link rel="stylesheet" type="text/css" />').attr('href', '++resource++pas.plugins.memberpropertytogroup.helper.css') );

(function() {
     jQuery(document).ready(function() {
        jQuery('.add_more_properties').on('click', function () {
            jQuery('#form div.field').each(function () {
                if (jQuery(this).hasClass('empty')) {
                    jQuery(this).removeClass('empty');
                    jQuery(this).next().removeClass('empty');
                    return false;
                }
            });

            jQuery('.remove_properties').prop("disabled", false);

            if (jQuery('#form').children('.empty').length === 0) {
                jQuery('.add_more_properties').prop("disabled", true);
            }
        });
        jQuery('.remove_properties').on('click', function () {
            if (jQuery('#form').has('.empty').length) {
                jQuery('#form div.field').each(function () {
                    if (jQuery(this).hasClass('empty')) {
                        jQuery(this).prev().children('textarea').val('');
                        jQuery(this).prev().prev().children('input').val('');
                        jQuery(this).prev().addClass('empty');
                        jQuery(this).prev().prev().addClass('empty');
                        return false;
                    }
                });

            } else {
                jQuery('#form div.field').last().children('textarea').val('');
                jQuery('#form div.field').last().addClass('empty');
                jQuery('#form div.field').last().prev().children('input').val('');
                jQuery('#form div.field').last().prev().addClass('empty');
            }

            jQuery('.add_more_properties').prop("disabled", false);

            if (jQuery('#form').children('.empty').length === 20) {
                jQuery('.remove_properties').prop("disabled", true);
            }
        });
     });
})(jQuery);
