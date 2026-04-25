$(document).ready(function(){
    console.log("ready!");

    const quizVal = $("#quizpage");

    $(".choice-box").click(function(){
        $(".choice-box").removeClass("bg-light border-primary");
        $(this).addClass("bg-light border-primary");
        $(this).find("input").prop("checked", true);
    });

    quizVal.submit(function(e)
    {
        e.preventDefault();

        var choice = $('input[name="answer"]:checked').val();

        if (choice != q["answer"])
        {
            $("#feedback").html(q["hint"]);
            return;
        }
        else
        {
            $(this).unbind('submit').submit();
        }
    })

});