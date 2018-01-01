function gameInfoOne(selected){
  switch (selected) {
    case 1:
        document.getElementById("mood").value = selected;
        select(document.getElementById("game_select_aa"));
        unselect(document.getElementById("game_select_ab"));
        unselect(document.getElementById("game_select_ac"));
        break;
    case 2:
        document.getElementById("mood").value = selected;
        unselect(document.getElementById("game_select_aa"));
        select(document.getElementById("game_select_ab"));
        unselect(document.getElementById("game_select_ac"));
        break;
    case 3:
        document.getElementById("mood").value = selected;
        unselect(document.getElementById("game_select_aa"));
        unselect(document.getElementById("game_select_ab"));
        select(document.getElementById("game_select_ac"));
        break;
  }
}
function moreOptions(){
  //shows more moreOptions
  document.getElementById("genres").style.display = "block";
  document.getElementById("categories").style.display = "block";
}
function selectOption(element){
  console.log('what');
  var input = element.childNodes[0];

  if(input.value == 1){
    input.value = 0;
    unselect(element);
  }else{
    input.value = 1;
    select(element);
  }
  console.log(input.value)
}
function select(element){
  element.style.transform = "translatey(2px)"
  element.style.backgroundColor = "#b5b5b5";
  element.style.boxShadow= "none";
}
function unselect(element){
  element.style.transform = "translatey(0px)"

    element.style.backgroundColor = "white";
    element.style.boxShadow= "1px 2px 1px #888888";
}
