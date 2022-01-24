document.addEventListener('DOMContentLoaded', function() {
    
    document.addEventListener('click', function(e) {
        if(e.target.id === 'search') {
            e.preventDefault();
            const search_input = document.querySelector('#search_input');
            const search_term = search_input.value
            const recipe_list = document.querySelector('#recipe_list');
            
            fetch(`/search/${search_term}`)
            .then(response => response.json())
            .then(recipes => {
                // Set title to search: search_term
                const page_title = document.querySelector('#page_title');
                page_title.innerHTML = `Search for "${search_term}"`;

                // Creat element that will recipe old recipe list
                const new_recipe_list = document.createElement('div');
                new_recipe_list.classList.add('container');

                // Check length of array that was fetched
                if(recipes.length === 0) {
                    new_recipe_list.innerHTML = 'No match.';
                } else {
                    // Display recipes on page
                    recipes.forEach(function(recipe) {
                        var recipe_title = document.createElement('li');
    
                        var recipe_url = document.createElement('a');
                        recipe_url.setAttribute('href', `/recipe_details/${recipe['id']}/`);
                        recipe_url.innerHTML = `${recipe['title']}`;
    
                        recipe_title.appendChild(recipe_url);
    
                        new_recipe_list.appendChild(recipe_title);
                    });
    
                }

                // Replace old recipes with new
                recipe_list.replaceWith(new_recipe_list);

                // Erase waht's writte in the search bar
                search_input.value = '';

                // Create div that will replace the pagination div
                const back_to_recipes_container = document.createElement('div');
                back_to_recipes_container.classList.add('container');

                // Create button that will take user back to recipes
                const back_to_recipes_button = document.createElement('button');
                back_to_recipes_button.classList.add('btn');
                back_to_recipes_button.classList.add('btn-primary');
                back_to_recipes_button.id = 'back_to_recipes';
                back_to_recipes_button.type = 'button';
                back_to_recipes_button.innerHTML = 'Back to My Recipes'
                back_to_recipes_container.appendChild(back_to_recipes_button);

                // Replace pagination with the back to recipes buttons
                const pagination = document.querySelector('#pagination');
                pagination.replaceWith(back_to_recipes_container);

            })
        } else if(e.target.id === 'back_to_recipes') {
            this.location.reload();
        }
    });

});