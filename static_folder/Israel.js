// function setup() {
//   // always put the elements in ""
//
//   $("#post").click(greeting);
// }


$(document).ready(() => {
  const commentContent = $('#comment-content');
  $('#comment-form').submit((event) => {
    event.preventDefault();
    $('#no-comments').remove();
    $('#comments')
        .append($('.user-comments')
            .append($('<h4>You wrote:</h4>'))
            .append($('<p/>', {text: commentContent.val()})));
    commentContent.val('');
    commentContent.focus();
  });
});

// $(document).ready(setup);
