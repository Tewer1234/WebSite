$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){

    $('#submit').click(function(){
        $.ajax({
            url: '/web_tool/ajax_data/', 
            data: $('#ajax_form').serialize(),
            success: function(response){ 
                try{
                    dd = JSON.parse(response.message);
                    window.alert("Success");
                    document.getElementById("message").style.display = "block";
                    document.getElementById("searchTbl").style.display="block";
                    $("#message").html("<div class='alert alert-success'> Successful </div>");
                    let text="";
                    for (var i=0;i<Object.keys(dd).length;i++){
                        text+=
                        '<tr>'+
                            '<td id="sg" class="text-center">'+dd[i].geneid+'</td>'+
                            '<td id="si" class="text-center">'+'<form id="transcript_form" action="/web_tool/index" target="_blank"><input class="rounded text-light tbl-element" id="transcriptid" type="submit" class="form-control" name="transcriptid" value="'+dd[i].transcript+'"> </form> </td>'+
                            '<td id="sn" class="text-center">' +dd[i].numbers+'</td>'+
                        '</tr>'
                    }
                    // window.alert(text);
                    $("#searchData").html(text);
                    document.getElementById("reset").style.display="inline-block";
                }catch{
                    $("#message").html("<div class='alert alert-danger'> Failed... </div>");
                    document.getElementById("searchTbl").style.display="none";
                    document.getElementById("reset").style.display="none";
                }
                    
            },
        });
    });
});

    $("#reset").click(function(){
            $.ajax({
                url: '/web_tool/ajax_data/', 
                data: $('#ajax_form').serialize(),
                success:function(){
                    var x=document.getElementById("message");
                    x.style.display = "none";
                    document.getElementById("ajax_form").reset();
                    document.getElementById("reset").style.display="none";
                    document.getElementById("searchTbl").style.display="none";
                }
            });
    });
