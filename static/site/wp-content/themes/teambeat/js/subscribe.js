jQuery(document).ready(function ($) {
  $('#registration-form').on('submit', function (e) {
    return
    e.preventDefault()
    e.stopPropagation()
    var email = $('#registration-email').val()
    console.log(email)
    $.ajax({
      type: 'post',
      url: 'https://app.teambit.io/api/users/register',
      data: {email: email},
      dataType: 'json',
      contentType: "application/json; charset=utf-8"
    })
    .done(function () {
      document.location = 'https://app.teambit.io/feedback'
    })
    .fail(function (e) {
      console.log(e)
    })
  })
      $('.subscribe-betalist').on('submit', function () {
        var $form = $(this),
            email = $('#email').val(),
            $btn = $form.find('button[type="submit"]');
        $.ajax({
            type: 'POST',
            url: 'https://app.teambit.io/api/users/betalist',
            data: {"email": email},
            dataType: 'json',
            beforeSend: function (data) {
                $btn.attr('disabled', 'disabled').html('<i class="icon-spin4 animate-spin"></i>');
            },
            error: function (err) {
                $form.find('p').after('<div class="notice">Error :( <a href="#" class="icon-remove"><i class="icon-cancel"></i></a></div>');
                $btn.text('You are subscribed');
            },
            success: function (data) {
                console.log(data)
                if (data.result != "success") {
                    // Something went wrong, do something to notify the user. maybe alert(data.msg);
                    $form.find('p').after('<div class="notice">Error :( <a href="#" class="icon-remove"><i class="icon-cancel"></i></a></div>');
                    $btn.text('You are subscribed');
                } else {
                    // It worked, carry on...
                    $btn.html('<i class="icon-ok"></i>');
                    $('#MERGE0').val('');
                }
            },
            complete: function (data) {
                $btn.prop('disabled', false);
            }
        });
        return false;
    });
    $('#subscribe').on('submit', function () {
        var $form = $(this),
      email = $('#MERGE0').val(),
            $btn = $form.find('button[type="submit"]');
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize(),
            cache: false,
            dataType: 'jsonp',
            jsonp: 'c',
            contentType: "application/json; charset=utf-8",
            beforeSend: function (data) {
                $btn.attr('disabled', 'disabled').html('<i class="icon-spin4 animate-spin"></i>');
            },
            error: function (err) {
                $form.find('p').after('<div class="notice">Error :( <a href="#" class="icon-remove"><i class="icon-cancel"></i></a></div>');
                $btn.text('You are subscribed');
            },
            success: function (data) {
                if (data.result != "success") {
                    // Something went wrong, do something to notify the user. maybe alert(data.msg);
                    $form.find('p').after('<div class="notice">Error :( <a href="#" class="icon-remove"><i class="icon-cancel"></i></a></div>');
                    $btn.text('You are subscribed');
                } else {
                    // It worked, carry on...
                    $btn.html('<i class="icon-ok"></i>');
                    $('#MERGE0').val('');
                }
            },
            complete: function (data) {
                $btn.prop('disabled', false);
            }
        });
        return false;
    });
});
