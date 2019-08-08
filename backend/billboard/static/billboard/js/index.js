
$(document).ready(function () {
    let addNewPost = function () {
        $('#addBtn').click(function () {
            $('<div id="inputPostWrap" class = "post-field"></div>').prependTo($('#spaceForPosts'));
            $('<div id="inputPostField" class = "post-infield"></div>').prependTo($('#inputPostWrap'));
            // body
            $('<div class = "post-content"><textarea id="contentBodyInput"  class="postInputContent"></textarea><button class="addPost-btn" id="finishedPostADD">DONE!</button></div>').prependTo($('#inputPostField'));
            // text between
            $('<h2 id="title" class = "post-header">content</h2>').prependTo($('#inputPostField'))
            // TITLe
            $('<div id="postHeader" class = "post-header">Title: <input id="NewPostTitleInput" class="postInputHeader"></input></div>').prependTo($('#inputPostField'));
            $("#addBtn").unbind();
            $('#finishedPostADD').click(function () {
                if ($('#NewPostTitleInput').val() !== "" && $('#contentBodyInput').val() !== "") {
                    $.ajax({
                        type: "POST",
                        url: "http://127.0.0.1:8000/billboard/create/",
                        data: JSON.stringify({ "post_title": $('#NewPostTitleInput').val(), "post_content": $('#contentBodyInput').val(), "post_author": "og" }),
                        success: console.log("worked"),
                        contentType: "application/json",
                        dataType: "json"
                    });

                }

                $("#inputPostWrap").remove();
            });
        });


    }

    addNewPost();
});



