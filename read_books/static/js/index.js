
function inputForm() {  
    // analyze the text into the form to the server
    
      form = document.querySelector("#usertext-form");
      
      form.addEventListener("submit", function(event)  {
          event.preventDefault();

          fetch("/ajax", {
            method:"post",
            body: new FormData(form),
            dataType: "json",
            })
          
          .then(response => response.json())
    
          .then(function (json) {console.log
              let query ={

                  title:json["title"],
                  response:json["response"],
                  picture:json["picture"],
                  author:json["author"]
                  
              };

              let newDiv_3 = document.createElement("div");
              newDiv_3.className = "title_cat_home";
              newDiv_3.innerHTML = "Result";
              let newDiv_5 = document.createElement("div");
              newDiv_5.className = "response_box";
              newDiv_5.id = "imessages-text_2";
              newDiv_5.innerHTML = query["picture"];
              document.getElementById("imessages-title").appendChild(newDiv_3);
              document.getElementById("imessages-title").appendChild(newDiv_5);

              

              });


})
}