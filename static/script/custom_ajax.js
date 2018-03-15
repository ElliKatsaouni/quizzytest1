$(document).ready(function() {
    $('.upVotes').click(function(){
        var quizid, userid;
        quizid = $(this).attr("data-quizid");
        userid = $(this).attr("data-userid");
        $.get('/quizzy/like', {quiz_id: quizid, user_id: userid}, function(data){
            $('#upVotes_count-' + quizid).html(data);
                $('#upVotes_button-'+quizid).prop('disabled', true);
                $('#downVotes_button-'+quizid).prop('disabled', true);
        });
    });

    $('.downVotes').click(function(){
        var quizid, userid;
        quizid = $(this).attr("data-quizid");
        userid = $(this).attr("data-userid");
        $.get('/quizzy/dislike/', {quiz_id: quizid, user_id: userid}, function(data){
            $('#downVotes_count-'+quizid).html(data);
                $('#downVotes_button-'+quizid).prop('disabled', true);
                $('#upVotes_button-'+quizid).prop('disabled', true);
        });
    });

    $('.favorite').click(function(){
        var quizid, userid;
        quizid = $(this).attr("data-quizid");
        userid = $(this).attr("data-userid");
        $.get('/quizzy/favorite/', {quiz_id: quizid, user_id: userid}, function(data){
            $('#favorite-'+quizid).prop('disabled', true);
            $('#unfavorite-'+quizid).prop('disabled', true);
        });
    });

    $('.unfavorite').click(function(){
        var quizid, userid;
        quizid = $(this).attr("data-quizid");
        userid = $(this).attr("data-userid");
        $.get('/quizzy/favorite/', {quiz_id: quizid, user_id: userid}, function(data){
            $('#unfavorite-'+quizid).prop('disabled', true);
            $('#favorite-'+quizid).prop('disabled', true);
        });
    });

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/quizzy/suggest/', {suggestion: query}, function(data){
            $('#pubsuggestions').empty();
            $('#pubsuggestions').html(data);
        });
    });

});
