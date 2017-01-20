$(document).ready(function() {
  $('.btn.favorite').click(function() {
      var $obj = $(this);
      var target_id = $obj.attr('id').split('_')[1];
      $obj.prop('disabled', true);
      $.ajax({
      url: $obj.attr('href'),
      type: 'POST',
      data: {target_model: $obj.attr('model'),
             target_object_id: target_id},
      success: function(response) {
          if (response.status == 'added') {
            $(".favorite-" + target_id).removeClass('fa-heart-o').addClass('fa-heart');
          }
          else {
            $(".favorite-" + target_id).removeClass('fa-heart').addClass('fa-heart-o');
          }
          $(".fav-count-" + target_id).load("  .fav-count-" + target_id);
          $obj.prop('disabled', false);
      }
      });
  });

  $('.btn.unfave').click(function() {
    var $obj = $(this);
    $obj.prop('disabled', true);
    $.ajax({
      url: $obj.attr('href'),
      type: 'POST',
      data: {
        target_model: $obj.data('model'),
        target_object_id: $obj.data('id')
      },
      success: function(response) {
        if (response.status == 'deleted') {
          $obj.parent().remove();
        }
      },
      complete: function(response) {
        $obj.prop('disabled', false);
      }
    });
  });
});