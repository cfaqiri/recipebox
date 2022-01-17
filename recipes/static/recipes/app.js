document.addEventListener('DOMContentLoaded', function() {
    
    document.addEventListener('mouseover', function(e) {
        if(e.target.className === 'recipe_index') {
            console.log("it's workin!");
        }
    });

});