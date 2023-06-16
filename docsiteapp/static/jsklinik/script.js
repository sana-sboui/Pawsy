let filterarray = [];
let vetarray = [
{
    id:1,
    name :"Ines Arfa",
    src :  "{% static 'C:/Users/sboui/Desktop/webpage/docsite/docsiteapp/static/img/team-1.jpg' %}"  ,
    desc :"5 Bis rue el Masjed El Aksa Cité El Ghazela Ariana، 2083"
},
{
    id:2,
    name :"Sofiene EL Ali",
    src : "{% static 'C:/Users/sboui/Desktop/webpage/docsite/docsiteapp/static/img/team-1.jpg' %}" ,
    desc :"15, 2 Rue sod maarab, Ariana 2037"
},
// and so on...
]
showvet(vetarray);
function showvet(currarray){
    document.getElementById("card").innerText = "";
    for(var i=0;i<currarray.length;i++){
        document.getElementById("card").innerHTML += `
                <div class="col-md-4 mt-3">
                <div class="card p-3 ps-5 pe-5">
                    <h4 class="text-capitalize text-center">${currarray[i].name}</h4> 
                    <img src="${currarray[i].src}" width="100%" height="320px"/>
                    <p class="mt-2">${currarray[i].desc}</p>
                    <button class="btn btn-primary w-100 mx-auto">More</button>
                </div >   
                </div>
        `
        
    }
}

document.getElementById("myinput").addEventListener("keyup",function(){
   let text = document.getElementById("myinput").value;
   filterarray = vetarray.filter(function(a){
        if(a.name.includes(text)){
            return a.name;
        }

   });
   if(this.value ==""){
    showvet(vetarray);
   }
else{
    if(filterarray ==""){
        document.getElementById("para").style.display = 'block' ;
        document.getElementById("card").innerHTML ="";
    }
    else{
        showvet(filterarray);
        document.getElementById("para").style.display = 'none';
    }
}

})
