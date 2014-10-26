$(document).ready(function() {

function vote (entryID) {
    $.ajax({
        type: "POST",
        url: "/vote/",
        data: {"entry": entryID},
        success: function() {
            $("#entry-vote-" + entryID).css({"color": " green "});
        }
    });
    return false;
}

$("a.vote").click(function() {
    var entryID =  parseInt(this.id.split("-")[2]);
    return vote(entryID);
})

});
