;(function ($) {
   $(function () {
       $(".button-collapse").sideNav();
       $("input[name='birth_date']").pickadate({
            selectMonths: true,
            selectYears: 60
        });
   });
})(jQuery);
