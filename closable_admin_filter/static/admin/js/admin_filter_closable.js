(function ($) {
    'use strict';
    $(function () {
        $('.module.filtered').attr('style', 'background: none!important;');
        var $hide_filter = $('<a href="#" id="hide_filter">СКРЫТЬ</a>');
        $hide_filter.css({
            'padding': '12px',
            'display': 'block',
            'text-align': 'center',
            'background': '#fff',
            'font-weight': 'bold'
        });
        $hide_filter.click(function () {
            var $next = $(this).nextAll().not('script');
            if ($next.is(':visible')) {
                $next.slideUp();
                $(this).text('ПОКАЗАТЬ');
            } else {
                $next.slideDown();
                $(this).text('СКРЫТЬ');
            }
        });
        $('#changelist-filter').find('h2:first').after($hide_filter).end().css('border', '#ccc 1px solid');
    });
})(django.jQuery);