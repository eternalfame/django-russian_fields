(function ($) {
    'use strict';
    var text_hide = gettext('Hide');
    var text_show = gettext('Show');

    $(function () {
        var $hide_filter = $('<a href="#" id="hide_filter">' + text_hide + '</a>');
        $hide_filter.click(function () {
            var $next = $(this).nextAll().not('script'); // avoid showing scripts
            if ($next.is(':visible')) {
                $next.slideUp();
                $(this).text(text_show);
            } else {
                $next.slideDown();
                $(this).text(text_hide);
            }
        });
        $('#changelist-filter').find('h2:first').after($hide_filter);
    });
})(django.jQuery);