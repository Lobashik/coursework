var current_id = "";


document.getElementById("2").addEventListener("click", function() {
    document.getElementById("muscle_groups").style.display = "none";
    document.getElementById("legs").style.display = "flex";
    current_id = "legs";
    document.getElementById("backbutton_" + current_id).addEventListener("click", function() {
        document.getElementById(current_id).style.display = "none";
        document.getElementById("muscle_groups").style.display = "flex";
    });
});

document.getElementById("1").addEventListener("click", function() {
    document.getElementById("muscle_groups").style.display = "none";
    document.getElementById("arms").style.display = "flex";
    current_id = "arms";
    document.getElementById("backbutton_" + current_id).addEventListener("click", function() {
        document.getElementById(current_id).style.display = "none";
        document.getElementById("muscle_groups").style.display = "flex";
    });
});

document.getElementById("3").addEventListener("click", function() {
    document.getElementById("muscle_groups").style.display = "none";
    document.getElementById("chest").style.display = "flex";
    current_id = "chest";
    document.getElementById("backbutton_" + current_id).addEventListener("click", function() {
        document.getElementById(current_id).style.display = "none";
        document.getElementById("muscle_groups").style.display = "flex";
    });
});

document.getElementById("4").addEventListener("click", function() {
    document.getElementById("muscle_groups").style.display = "none";
    document.getElementById("back").style.display = "flex";
    current_id = "back";
    document.getElementById("backbutton_" + current_id).addEventListener("click", function() {
        document.getElementById(current_id).style.display = "none";
        document.getElementById("muscle_groups").style.display = "flex";
    });
});

document.getElementById("5").addEventListener("click", function() {
    document.getElementById("muscle_groups").style.display = "none";
    document.getElementById("abdominals").style.display = "flex";
    current_id = "abdominals";
    document.getElementById("backbutton_" + current_id).addEventListener("click", function() {
        document.getElementById(current_id).style.display = "none";
        document.getElementById("muscle_groups").style.display = "flex";
    });
});