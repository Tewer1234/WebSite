$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){

    $("#browseSubmit").click(function(){
        $.ajax({
            url: '/web_tool/browse_data/', 
            data: $('#browse_form').serialize(),
            success: function(response){ 
                window.alert("Success");
                document.getElementById("searchTbl2").style.display="none";
                document.getElementById("basicInfo").style.display="none";
                document.getElementById("reset2").style.display="none";
                document.getElementById("next").style.display="none";
                document.getElementById("prev").style.display="none";
                document.getElementById("cnt").style.display="block";
                

                dd = JSON.parse(response.message4);
                text = "";
                var totalRows = Object.keys(dd).length;
                $("#browseBody").html("");

                var table="#browseBody";
                var maxRows,pageNum,totalRows,cur;

                document.getElementById("maxRows").ariaValueNow="0";
                document.getElementById("maxRows").selectedIndex="Select";
                document.getElementById("pageNumber").style.display="none";
                $("#maxRows").on("change", function(){
                    $(table).html("");
                    maxRows=parseInt($(this).val());
                    totalRows = Object.keys(dd).length;
                    cur=1;
                    pageNum = Math.ceil(totalRows/maxRows);
                    text="";

                    for (var i=0;i<Math.min(totalRows,maxRows);i++){
                    text+="<tr>";
                    text+='<td id="sn" class="text-center">' + dd[i]["Gene ID"] + '</td>'+
                    '<td id="sn" class="text-center">' + dd[i]["Status"] + '</td>'+
                    '<td id="sn" class="text-center">' + dd[i]["Sequence"] + '</td>'+
                    '<td id="sn" class="text-center">' + dd[i]["Gene Name"] + '</td>'+
                    '<td id="sn" class="text-center">' + dd[i]["Other Name"] + '</td>'+
                    '<td id="sn" class="text-center"><form id="transcript_form3" action="/web_tool/index2" target="_blank"><input class="rounded text-light tbl-element" id="transcriptid3" type="submit" class="form-control" name="transcriptid3" value="'+dd[i]["Transcript"]+'"> </form></td>'+
                    '<td id="sn" class="text-center">' + dd[i]["Type"] + '</td>'+
                    "</tr>"
                    }

                    check();
                    // var inh = toString(cur)+" of "+ toString(pageNum) + "Pages";
                    // document.getElementById("pageNumber").innerHTML=inh;
                    document.getElementById("pageNumber").style.display="inline";
                    $("#browseBody").html(text);
                })


                $("#prev").on("click", function(){
                    if (cur-1>=1){
                        cur--;
                        text="";
                        for (var i=((cur-1)*maxRows);i<Math.min(totalRows,cur*maxRows);i++){
                            // console.log(dd[i]["Gene ID"]);
                            text+="<tr>";
                            text+='<td id="sn" class="text-center">' + dd[i]["Gene ID"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Status"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Sequence"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Gene Name"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Other Name"] + '</td>'+
                            '<td id="sn" class="text-center"><form id="transcript_form3" action="/web_tool/index2" target="_blank"><input class="rounded text-light tbl-element" id="transcriptid3" type="submit" class="form-control" name="transcriptid3" value="'+dd[i]["Transcript"]+'"> </form></td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Type"] + '</td>'+
                            "</tr>"
                        }
                        $("#browseBody").html(text);
                    }
                    check();
                })

                $("#next").on("click", function(){
                    if (cur+1<=pageNum){
                            document.getElementById("prev").style.display="inline";
                            document.getElementById("next").style.display="inline";
                                    console.log("Next",cur);
                        cur++;
                        text="";
                        for (var i=((cur-1)*maxRows);i<Math.min(totalRows,cur*maxRows);i++){
                            text+="<tr>";
                            text+='<td id="sn" class="text-center">' + dd[i]["Gene ID"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Status"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Sequence"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Gene Name"] + '</td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Other Name"] + '</td>'+
                            '<td id="sn" class="text-center"><form id="transcript_form3" action="/web_tool/index2" target="_blank"><input class="rounded text-light tbl-element" id="transcriptid3" type="submit" class="form-control" name="transcriptid3" value="'+dd[i]["Transcript"]+'"> </form></td>'+
                            '<td id="sn" class="text-center">' + dd[i]["Type"] + '</td>'+
                            "</tr>"
                        }
                        $("#browseBody").html(text);
                    }
                    check();
                })     
                
                function check() {
                    if (pageNum!=1){
                        if (cur==1){
                            document.getElementById("prev").style.display="none";
                            document.getElementById("next").style.display="inline";
                        }
    
                        if (cur<pageNum) document.getElementById("next").style.display="inline";
                        else document.getElementById("next").style.display="none";
                        
                        if (cur>1) document.getElementById("prev").style.display="inline";
                        else document.getElementById("prev").style.display="none";
                    }    
                    var inh = String(cur)+" / "+ String(pageNum);
                    document.getElementById("pageNumber").innerHTML=inh;
                }
                
                
                document.getElementById("browseTbl").style.display="block";
            },error: function(){
                alert("Wrong");
                document.getElementById("browseTbl").style.display="none";
            }
        });
    });
});