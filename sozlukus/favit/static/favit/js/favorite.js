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
            $obj.children().removeClass('icon-heart-empty').addClass('icon-heart');}
          else {
            $obj.children().removeClass('icon-heart').addClass('icon-heart-empty');
          }
          $obj.parent('.favit').children('.fav-count').text(response.fav_count);
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
