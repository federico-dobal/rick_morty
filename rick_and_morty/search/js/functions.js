function myFunction(value, products) {

  console.log('update', value);

  let html = '<ul><h1>Search Results</h1>';

  for (product of products) {

    if (value === undefined || product.name.toLowerCase().indexOf(value.toLowerCase()) !== -1) {

      html += '<article>';
        html += '<div>'
          html += '<div class="section">'
              html += '<a href="' + product.image + '"rel="nofollow noopener noreferrer" target="_blank">'
                html += '<h2>' + product.name + '</h2>'
              html += '</a>'
          html += '</div>'
        html += '</div>'
        html += '<div>'
          html += '<img src="'+ product.image + '" alt="'+ product.name + '">'
        html += '</div>'

      html += '</article>'

    }
  }

  html += '</ul>'

  document.getElementById("proposed_results").innerHTML =  html;
}
