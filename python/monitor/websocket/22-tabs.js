document.addEventListener('DOMContentLoaded', function(event) { 
  const tabHeaders  = document.getElementsByClassName('tab-headers')[0];
  const tabContents = document.getElementsByClassName('tab-contents')[0];
      
  Array.from(tabHeaders.children).forEach((targetHeader) => {
    // Tab Headers: All Click Events
    targetHeader.addEventListener('click', () => {
      const targetName = targetHeader.dataset.target;
      const colorClass = targetHeader.dataset.color;
      const targetContent = document.getElementById(targetName);

      // Set all to default setting
      Array.from(tabHeaders.children).forEach((tabHeader) => {
        tabHeader.classList.remove('is-active');
        tabHeader.classList.remove(tabHeader.dataset.color);
      });
      // Except the chosen one
      targetHeader.classList.add('is-active');
      targetHeader.classList.add(colorClass);

      // Showing the content
      Array.from(tabContents.children).forEach((tabContent) => {
        tabContent.style.display = 'none';
      });
      targetContent.style.display = 'block';
      targetContent.classList.add(colorClass);
    });
  });

  // Tab Headers: Default
  tabHeaders.getElementsByClassName('is-active')[0].click();
});

document.addEventListener('DOMContentLoaded', function(event) {
  const tabHeaders  = document.getElementsByClassName('tab-headers')[0];

  const tabdelays = [
    { name: "progress", delay: 9000 },
    { name: "review",   delay: 7000 },
    { name: "report",   delay: 5000 }
  ]

  const tabNames = tabdelays.flatMap(item => item.name)
  tabName = "progress"

  function nextTabName(name) {
    let index = tabNames.indexOf(name) + 1
    return tabNames[index==tabNames.length ? 0 : index]
  }

  // Flexible Interval 
  const timeOutFunc = () => {
    const activeTab     = tabHeaders.
      getElementsByClassName('is-active')[0]
    const activeTabName = activeTab.dataset.target

    const targetName    = nextTabName(activeTabName)
    const targetTab     = "tab-" + targetName

    const targetItem = tabdelays.filter(
      item => item.name==targetName)
    const delay = targetItem[0].delay

    console.log(targetTab)
    document.getElementById(targetTab).click()

    // recursive
    setTimeout(timeOutFunc, delay)
  }
  
  setTimeout(timeOutFunc, 5000)

});

