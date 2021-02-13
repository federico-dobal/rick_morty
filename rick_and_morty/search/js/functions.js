/**
  Update search results based on the value on the search box by filtering the products
*/
function update_search_results_div(value, products) {

  let html = '<ul><h1>Search Results</h1>';

  for (product of products) {

    if (value === undefined || product.name.toLowerCase().indexOf(value.toLowerCase()) !== -1) {
      html += '<article>';
      html += '<div>'
      html += '<div class="section">'
      html += '<a href="' + product.image + '"rel="nofollow noopener noreferrer" target="_blank">'
      html += '<h2>' + product.name + '</h2>'
      html += '</a>'
      html += '<ul>'
      html += '<li><b>Status</b>: ' + product.status + '</li>'
      html += '<li><b>Gender</b>: ' + product.gender + '</li>'
      html += '<li><b>Species</b>: ' + product.species + '</li>'
      html += '</ul>'
      html += '</div>'
      html += '</div>'
      html += '</br>'
      html += '<div>'
      html += '<img src="'+ product.image + '" alt="'+ product.name + '">'
      html += '</div>'
      html += '</article>'
    }

  }

  document.getElementById("proposed_results").innerHTML =  html;
}
