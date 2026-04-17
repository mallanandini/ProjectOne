function confirmDelete() {
    return confirm("Are you sure you want to delete this student?");
}

function validateForm() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let course = document.getElementById("course").value;

    if (name === "" || email === "" || course === "") {
        alert("All fields must be filled out");
        return false;
    }
    return true;
}

//search 
document.addEventListener("DOMContentLoaded", function() {
    const search = document.getElementById("search");
    if (search) {
        search.addEventListener("keyup", function() {
            // Handle search functionality
            search.value.toLowerCase();
            let cards = document.querySelectorAll(".card");
            cards.forEach(function(card) {
                card.style.display = card.innerText.toLowerCase().includes(search.value)
                ? "block" : "none";
            });
        });
    }
});

