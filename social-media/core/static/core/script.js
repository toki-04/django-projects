
const dashboard_icon = document.getElementById("dashboard-icon")
const community_icon = document.getElementById("community-icon")
const chat_icon = document.getElementById("chat-icon")
const settings_icon= document.getElementById("settings-icon")
function nav_mouse_over(img_name){
  if (img_name === "dashboard"){
    dashboard_icon.src="/static/core/images/selected-dashboard.png"
  }

  else if (img_name === "community"){
    community_icon.src="/static/core/images/selected-community.png"
  }

  else if (img_name === "chat"){
    chat_icon.src="/static/core/images/selected-bubble-chat.png"
  }
  else if (img_name === "settings"){
    settings_icon.src="/static/core/images/selected-settings.png"
  }
}

function nav_mouse_leave(img_name, selected=false){
  if (selected === true){
    return
  }

  if (img_name === "dashboard"){
    dashboard_icon.src="/static/core/images/dashboard.png"
  }

  else if (img_name === "community"){
    community_icon.src="/static/core/images/community.png"
  }

  else if (img_name === "chat"){
    chat_icon.src="/static/core/images/bubble-chat.png"
  }
  else if (img_name === "settings"){
    settings_icon.src="/static/core/images/settings.png"
  }
}


function create_post_modal(){
  return
}
