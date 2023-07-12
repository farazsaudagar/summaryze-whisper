document.getElementById("summaryze").addEventListener("click", async() => {
    const tab = await getCurrentTab()
    if(!tab) return alert('Require an active tab')
    chrome.scripting.executeScript({
        target: { tabId: tab.id},
        files: ['index.js']
    })
}) 

async function getCurrentTab() {
    const queryOptions = { active: true, lastFocusedWindow: true } 
    const [tab] = await chrome.tabs.query(queryOptions)
    return tab
}