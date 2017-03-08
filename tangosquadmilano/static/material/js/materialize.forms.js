(function() {
  function initForms ($container) {
    // Formsets
    // https://bitbucket.org/ionata/django-formset-js
    $('.formset-field').formset({
      animateForms: true,
      newFormCallback: initForms
    })

    // Select
    // http://materializecss.com/forms.html#select
    $container
      .find('select')
      .not('.disabled')
      .not('.material-ignore')
      .material_select()

    // Date/DateTime/Time
    // https://github.com/xdan/datetimepicker
    // Overriding jquery date controller with materialize one
    // for certain fields
    $container
      .find('[data-form-control="date"]')
      .each(function () {
        if($(this).attr("name") == "birth_date"){
          $(this).pickadate({
            format: "yyyy-mm-dd",
            selectMonths: true,
            selectYears: 100,
            max: 2017,
          })
        }
        else{
          $(this).datetimepicker({
            format: this.dataset.dateFormat,
            timepicker: false,
            mask: false,
            scrollInput: false
          })
        }
      })
    $container
      .find('[data-form-control="time"]')
      .each(function () {
        $(this).datetimepicker({
          format: this.dataset.dateFormat,
          datepicker: false,
          timepicker: true,
          mask: false,
          scrollInput: false
        })
      })
    $container.find('[data-form-control="datetime"]').each(
      function () {
        $(this).datetimepicker({
          format: this.dataset.dateFormat,
          datepicker: true,
          timepicker: true,
          mask: false,
          scrollInput: false
        })
      })
  }

  $(document).on('ready turbolinks:load', function() { initForms($(document)) })
})()
