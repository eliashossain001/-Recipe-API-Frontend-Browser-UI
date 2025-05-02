let page = 1;
let limit = 15;

function loadRecipes(resetPage = false) {
    if (resetPage) page = 1;

    const title = document.getElementById('searchTitle').value;
    const cuisine = document.getElementById('searchCuisine').value;
    const rating = document.getElementById('searchRating').value;
    limit = document.getElementById('pageLimit').value;

    let url = `/api/recipes/?page=${page}&limit=${limit}`;

    if (title) url += `&search=${title}`;
    if (cuisine) url += `&cuisine=${cuisine}`;
    if (rating) url += `&rating=${rating}`;

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const table = document.getElementById('recipeTable');
        table.innerHTML = "";

        if (!data.data || data.data.length === 0) {
            document.getElementById('noResults').classList.remove('d-none');
            document.getElementById('pageInfo').innerText = '';
        } else {
            document.getElementById('noResults').classList.add('d-none');

            data.data.forEach(recipe => {
                const tr = document.createElement('tr');
                tr.classList.add('clickable');
                tr.onclick = () => showDetail(recipe);

                tr.innerHTML = `
                    <td class="truncate">${recipe.title}</td>
                    <td>${recipe.cuisine || '-'}</td>
                    <td>${getStars(recipe.rating)}</td>
                    <td>${recipe.total_time} mins</td>
                    <td>${recipe.serves}</td>
                `;
                table.appendChild(tr);
            });

            document.getElementById('pageInfo').innerText = `Page ${data.page}`;
        }
    });
}

function getStars(rating) {
    if (!rating) return "-";
    const stars = Math.round(rating);
    return "★".repeat(stars) + "☆".repeat(5 - stars);
}

function prevPage() {
    if (page > 1) {
        page--;
        loadRecipes();
    }
}

function nextPage() {
    page++;
    loadRecipes();
}

function showDetail(recipe) {
    document.getElementById('modalTitle').innerText = `${recipe.title} (${recipe.cuisine})`;

    let modalBody = `
        <p><strong>Description:</strong> ${recipe.description}</p>
        <p><strong>Total Time:</strong> ${recipe.total_time} mins 
        <br><small>Prep Time: ${recipe.prep_time} mins, Cook Time: ${recipe.cook_time} mins</small></p>
        <h5>Nutrition</h5>
        <table class="table">
            <thead><tr><th>Type</th><th>Value</th></tr></thead>
            <tbody>
    `;

    for (const [key, value] of Object.entries(recipe.nutrients)) {
        modalBody += `<tr><td>${key}</td><td>${value}</td></tr>`;
    }

    modalBody += `</tbody></table>`;

    document.getElementById('modalBody').innerHTML = modalBody;

    const modal = new bootstrap.Modal(document.getElementById('detailModal'));
    modal.show();
}

document.addEventListener('DOMContentLoaded', () => {
    loadRecipes();

    document.getElementById('searchButton').addEventListener('click', () => {
        loadRecipes(true);  // Reset to page 1 on search
    });
});
