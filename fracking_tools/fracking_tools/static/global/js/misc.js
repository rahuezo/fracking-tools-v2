function setCollapseArrow(element) {
  let icon = $(element).find('svg').data('icon');


  if (icon === 'angle-double-down') {
    console.log('inside', icon);
    // $(element).html(`<i class='fas fa-angle-double-up'></i>`);
    $(element).text(`<h1>HELLO</h1>`);
  } {
    $(element).html(`<i class='fas fa-angle-double-down'></i>`);
  }
  // $(this).html() === `<i class='fas fa-angle-double-down'></i>` ? $(this).html(`<i class='fas fa-angle-double-down'></i>`) : $(this).html(`<i class='fas fa-angle-double-up'></i>`);
}
