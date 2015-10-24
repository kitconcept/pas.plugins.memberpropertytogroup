jQuery('head').append( jQuery('<link rel="stylesheet" type="text/css" />').attr('href', '++resource++pas.plugins.memberpropertytogroup.helper.css') );

(function() {
     jQuery(document).ready(function() {

        // Emulate initial markup of in Plone 4 where fields with empty values
        // have a class 'empty' attached.
        // jQuery('#form div.field').each(function() {
        //   var div = jQuery(this);
        //   if (div.children('input').val() === '') {
        //     div.addClass('empty');
        //   } else if (div.children('textarea').val() === '') {
        //     div.addClass('empty');
        //   }
        // });

        if (parseInt(jQuery('#form-widgets-showing_fields').val()) > 1) {
            jQuery('.remove_properties').attr("disabled", false);
        }

        if (parseInt(jQuery('#form-widgets-showing_fields').val()) == 10) {
            jQuery('.add_more_properties').attr("disabled", true);
        }

        jQuery('.add_more_properties').bind('click', function (event) {
            event.preventDefault();
            var show_fields = jQuery('#form-widgets-showing_fields').val();
            var selector_gp = '#form-widgets-group_property_' + show_fields;
            var selector_vg = '#form-widgets-valid_groups_' + show_fields;
            jQuery(selector_gp).parent().parent().parent().removeClass('field-hidden');
            jQuery(selector_vg).parent().parent().parent().removeClass('field-hidden');

            jQuery('.remove_properties').attr("disabled", false);

            if (parseInt(show_fields) === 9) {
                jQuery('.add_more_properties').attr("disabled", true);
            }

            if (parseInt(show_fields) < 10) {
                var increment = (parseInt(show_fields) + 1).toString();
                jQuery('#form-widgets-showing_fields').val(increment);
            }

        });

        jQuery('.remove_properties').bind('click', function () {
            event.preventDefault();
            var show_fields = jQuery('#form-widgets-showing_fields').val();
            if (parseInt(show_fields) > 1) {
                var decrement = (parseInt(show_fields) - 1).toString();
                jQuery('#form-widgets-showing_fields').val(decrement);
                show_fields = jQuery('#form-widgets-showing_fields').val();
            }
            var selector_gp = '#form-widgets-group_property_' + show_fields;
            var selector_vg = '#form-widgets-valid_groups_' + show_fields;
            jQuery(selector_gp).parent().parent().parent().addClass('field-hidden');
            jQuery(selector_vg).parent().parent().parent().addClass('field-hidden');

            jQuery(selector_gp).val('');
            jQuery(selector_vg).val('');

            jQuery('.add_more_properties').attr("disabled", false);

            if (parseInt(show_fields) === 1) {
                jQuery('.remove_properties').attr("disabled", true);
            }

        });
     });
})(jQuery);
