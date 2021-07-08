document.addEventListener("DOMContentLoaded", function() {
    console.log("hello world")
    
    var container = document.getElementById("container")
    console.log(container.innerHTML)
    
    
    var title = document.getElementById("title")
    title.addEventListener("click", function(){
        console.log("THE H1 WAS CLICKED")
    })
    
    function handler(){
        console.log("this is a handler function")
    }
    title.addEventListener("mouseenter", handler)
    
    
    // 1. GRAB THE BUTTONS
    var dark_button = document.getElementById("dark_mode")
    var lite_button = document.getElementById("lite_mode")
    
    // 2. ADD EVENT LISTENERS AND CALLBACK FUNCTIONS
    var p_tags = document.getElementsByClassName('text')
    console.log(p_tags)
    
    dark_button.addEventListener("click", function(){
        container.style.backgroundColor = "black"
        for(var i = 0; i < p_tags.length;i++){
            p_tags[i].style.color = "white";
        }
    })
    
    
    lite_button.addEventListener("click", function(){
        container.style.backgroundColor = "ivory"
        for(var i = 0; i < p_tags.length;i++){
            p_tags[i].style.color = "black";
        }
    })

    
    
});