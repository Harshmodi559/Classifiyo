

function myFunction(id)
{   
    // console.log(id)
   var check_id=document.getElementById(id)
//    console.log(check_id)
    if(check_id.classList.contains("checked"))
    {
        // console.log("already have class")
        var id_=id;
        for (var i=1;i<6;i++){
            var a=document.getElementById(i);
            // if(check_id.classList.contains("checked"))
            // {
                a.classList.remove("checked")}

            // }
        document.getElementById("demo").innerHTML="";
  
        // check_id.classList.remove("checked")
    }
    else{
        // console.log("not have")
    for (var i=1;i<=id;i++){
    var a=document.getElementById(i)
    a.classList.add("checked") 
    }
    const grade=["Very Bad","Not Good","good","Nice","Excellent"]
    document.getElementById("demo").innerHTML=grade[id-1]
    }


}

// a.addEventListener("click", myFunction());
// b.addEventListener("click", myFunction());
// c.addEventListener("click", myFunction());
// d.addEventListener("click", myFunction());
// e.addEventListener("click", myFunction());