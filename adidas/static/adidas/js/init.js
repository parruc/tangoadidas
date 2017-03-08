;(function ($) {
   $(function () {
       $(".button-collapse").sideNav();
       // Disables old datepicked and add the new
       $("input[name='birth_date']").datetimepicker("destroy").pickadate({
            selectMonths: true,
            selectYears: 50,
            max: 2017,
        });
   });
})(jQuery);
