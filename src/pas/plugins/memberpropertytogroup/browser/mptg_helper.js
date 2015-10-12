$('head').append( $('<link rel="stylesheet" type="text/css" />').attr('href', '++resource++pas.plugins.memberpropertytogroup.helper.css') );

(function($) {
     $(document).ready(function() {
        $('.add_more_properties').on('click', function () {
            $('#form div.field').each(function () {
                if ($(this).hasClass('empty')) {
                    $(this).removeClass('empty');
                    $(this).next().removeClass('empty');
                    return false;
                }
            });

            $('.remove_properties').prop("disabled", false);

            if ($('#form').children('.empty').length === 0) {
                $('.add_more_properties').prop("disabled", true);
            }
        });
        $('.remove_properties').on('click', function () {
            if ($('#form').has('.empty').length) {
                $('#form div.field').each(function () {
                    if ($(this).hasClass('empty')) {
                        $(this).prev().children('textarea').val('');
                        $(this).prev().prev().children('input').val('');
                        $(this).prev().addClass('empty');
                        $(this).prev().prev().addClass('empty');
                        return false;
                    }
                });

            } else {
                $('#form div.field').last().children('textarea').val('');
                $('#form div.field').last().addClass('empty');
                $('#form div.field').last().prev().children('input').val('');
                $('#form div.field').last().prev().addClass('empty');
            }

            $('.add_more_properties').prop("disabled", false);

            if ($('#form').children('.empty').length === 20) {
                $('.remove_properties').prop("disabled", true);
            }
        });
     });
})(jQuery);
