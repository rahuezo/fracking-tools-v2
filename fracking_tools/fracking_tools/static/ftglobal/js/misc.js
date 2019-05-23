function setCollapseArrow(element) {
  let icon = $(element).find('svg').data('icon');

  if (icon === 'angle-double-down') {
    $(element).html(`<i class='fas fa-angle-double-up transparent-element'></i>`);
  } else {
    $(element).html(`<i class='fas fa-angle-double-down transparent-element'></i>`);
  }
}
