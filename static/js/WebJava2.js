$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){

    $('#submit2').click(function(){
        $.ajax({
            url: '/web_tool/ajax_data2/', 
            data: $('#ajax_form2').serialize(),
            success: function(response){ 
                try{
                    dd = JSON.parse(response.message2);
                    window.alert("Success");
                    document.getElementById("message2").style.display = "block";
                    document.getElementById("searchTbl2").style.display="block";
                    document.getElementById("basicInfo").style.display="block";
                    document.getElementById("cnt").style.display="none";
                    document.getElementById("next").style.display="none";
                    document.getElementById("pageNumber").style.display="none";

                    $("#message2").html("<div class='alert alert-success'> Successful </div>");
                    let text="",text1="",input=dd[0]["input"];
                    for (var i=0;i<Object.keys(dd).length;i++){
                        if (input!=dd[i]["Transcript"]){
                            text+=
                            '<tr>'+
                                '<td id="si" class="text-center">'+ '<form id="transcript_form2" action="/web_tool/index" target="_blank"><input class="rounded text-light tbl-element" id="transcriptid2" type="submit" class="form-control" name="transcriptid2" value="'+dd[i]["Transcript"]+'"> </form> </td>'+
                                '<td id="sn" class="text-center">' +dd[i]["Transcript Length (nt)"]+'</td>'+
                                '<td id="sn" class="text-center">' +dd[i]["Type"]+'</td>'+
                                '<td id="sn" class="text-center">' +dd[i]["Coding Sequence (CDS)"]+'</td>'+
                                '<td id="sn" class="text-center">' +dd[i]["Coding Sequence Length (nt)"]+'</td>'+
                                '<td id="sn" class="text-center">' +dd[i]["Protein"]+'</td>'+
                                '<td id="sn" class="text-center">' +dd[i]["Protein Length (aa)"]+'</td>'+
                            '</tr>'
                        }else{
                            text+=
                            '<tr>'+
                                '<td id="si" class="text-center" style="background-color:yellow">'+ '<form id="transcript_form2" action="/web_tool/index" target="_blank"><input class="rounded text-light tbl-element" id="transcriptid2" type="submit" class="form-control" name="transcriptid2" value="'+dd[i]["Transcript"]+'"> </form> </td>'+
                                '<td id="sn" class="text-center" style="background-color:yellow">' +dd[i]["Transcript Length (nt)"]+'</td>'+
                                '<td id="sn" class="text-center" style="background-color:yellow">' +dd[i]["Type"]+'</td>'+
                                '<td id="sn" class="text-center" style="background-color:yellow">' +dd[i]["Coding Sequence (CDS)"]+'</td>'+
                                '<td id="sn" class="text-center" style="background-color:yellow">' +dd[i]["Coding Sequence Length (nt)"]+'</td>'+
                                '<td id="sn" class="text-center" style="background-color:yellow">' +dd[i]["Protein"]+'</td>'+
                                '<td id="sn" class="text-center" style="background-color:yellow">' +dd[i]["Protein Length (aa)"]+'</td>'+
                            '</tr>'
                        }
                    }
                    if (input!=dd[0]["Gene ID"]){
                        text1+=
                        '<tr>'+
                        '<td scope="col" class="text-center">'+dd[0]["Gene ID"]+'</td>'+
                        '<td scope="col" class="text-center">'+dd[0]["Status"]+'</td>'+
                        '<td scope="col" class="text-center">'+dd[0]["Sequence"]+'</td>'+
                        '<td scope="col" class="text-center">'+dd[0]["Gene Name"]+'</td>'+
                        '<td scope="col" class="text-center">'+dd[0]["Other Name"]+'</td>';
                        text1+='<td scope="col" class="text-center"> <ul>'
                    }else{
                        text1+=
                        '<tr>'+
                        '<td scope="col" class="text-center" style="background-color:yellow">'+dd[0]["Gene ID"]+'</td>'+
                        '<td scope="col" class="text-center" style="background-color:yellow">'+dd[0]["Status"]+'</td>'+
                        '<td scope="col" class="text-center" style="background-color:yellow">'+dd[0]["Sequence"]+'</td>'+
                        '<td scope="col" class="text-center" style="background-color:yellow">'+dd[0]["Gene Name"]+'</td>'+
                        '<td scope="col" class="text-center" style="background-color:yellow">'+dd[0]["Other Name"]+'</td>';
                        text1+='<td scope="col" style="background-color:yellow" class="text-center"> <ul>'
                    }
                    
                    for (var i=0;i<Object.keys(dd).length;i++){
                        if (dd[i]["transcript"].length>=1){
                            text1+='<li>'+dd[i]["transcript"]+'</li>';
                        }
                    }
                    if (input!=dd[0]["Gene ID"]) text1+='</ul> </td><td scope="col" class="text-center"> <ul>';
                    else text1+='</ul> </td><td scope="col" style="background-color:yellow" class="text-center"> <ul>';
                    for (var i=0;i<Object.keys(dd).length;i++){
                        if (dd[i]["type"].length>=1){
                            text1+='<li>' + dd[i]["type"] + '</li>';
                        }
                    }
                    if (input!=dd[0]["Gene ID"]){
                        text1+='</ul></td>'+
                        '<td scope="col" class="text-center">'+dd[0]["Transcript Count"]+'</td>'+
                        '</tr>';
                    }else{
                        text1+='</ul></td>'+
                        '<td scope="col" style="background-color:yellow" class="text-center">'+dd[0]["Transcript Count"]+'</td>'+
                        '</tr>';
                    }

                    if (dd[0]["Transcript Count"]!=0){
                        $("#searchData2").html(text);
                    }else{
                        $("#searchData2").html("<h3 class='text-center col-sm-12'> No Data Available </h3>");
                    }
                    $("#basicData").html(text1);
                    $("#head").html("<h2>" + dd[0]["Gene ID"] + "</h2>");
                    document.getElementById("reset2").style.display="inline-block";
                    document.getElementById("browseTbl").style.display="none";
                }catch{
                    document.getElementById("message2").style.display = "block";
                    window.alert("Fail");
                    $("#message2").html("<div class='alert alert-danger'> Failed... </div>");
                    document.getElementById("searchTbl2").style.display="none";
                    document.getElementById("basicInfo").style.display="none";
                    document.getElementById("reset2").style.display="none";
                }
                    
            },
        });
    });
});

    $("#reset2").click(function(){
            $.ajax({
                url: '/web_tool/ajax_data2/', 
                data: $('#ajax_form2').serialize(),
                success:function(){
                    var x=document.getElementById("message2");
                    x.style.display = "none";
                    document.getElementById("ajax_form2").reset();
                    document.getElementById("reset2").style.display="none";
                    document.getElementById("searchTbl2").style.display="none";
                    document.getElementById("basicInfo").style.display="none";
                }
            });
    });

    
