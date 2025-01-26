function filterTable() {
    // Get the search input and table elements
    const searchInput = document.getElementById('searchBar');
    const filter = searchInput.value.toLowerCase();
    const table = document.getElementById('dataTable');
    const rows = table.getElementsByTagName('tr');
  
    // Loop through all table rows (skip the header row)
    for (let i = 1; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName('td');
      let rowContainsSearchTerm = false;
  
      // Check if any cell in the row contains the search term
      for (let j = 0; j < cells.length; j++) {
        const cellText = cells[j].textContent || cells[j].innerText;
        if (cellText.toLowerCase().includes(filter)) {
          rowContainsSearchTerm = true;
          break;
        }
      }
  
      // Show or hide the row based on the search term
      rows[i].style.display = rowContainsSearchTerm ? '' : 'none';
    }
  }
  