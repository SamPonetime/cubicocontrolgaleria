document.querySelectorAll(".card_projects img").forEach(el=>{
    el.addEventListener("click", function(ev){
     ev.stopPropagation();
     this.parentNode.classList.add("active");
   })
   });
   
   document.querySelectorAll(".card_projects").forEach(el=>{
    el.addEventListener("click", function(ev){
      this.classList.remove("active");
      console.log("click")
      
    }) 
   })
   
   