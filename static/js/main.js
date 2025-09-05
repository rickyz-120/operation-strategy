// Main JavaScript for Wise Routes Application

document.addEventListener("DOMContentLoaded", () => {
  // Update current date and time
  updateDateTime()
  setInterval(updateDateTime, 1000)

  // Initialize page-specific functionality
  initializePageFeatures()

  // Add smooth animations
  addAnimations()
})

function updateDateTime() {
  const now = new Date()
  const options = {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }

  const datetimeElement = document.getElementById("current-datetime")
  if (datetimeElement) {
    datetimeElement.textContent = now.toLocaleDateString("pt-BR", options)
  }
}

function initializePageFeatures() {
  // Add click effects to neumorphic buttons
  const buttons = document.querySelectorAll(".neu-button")
  buttons.forEach((button) => {
    button.addEventListener("mousedown", function () {
      this.style.transform = "translateY(2px)"
      this.style.boxShadow = "inset 3px 3px 6px var(--shadow-dark), inset -3px -3px 6px var(--shadow-light)"
    })

    button.addEventListener("mouseup", function () {
      this.style.transform = "translateY(0)"
      this.style.boxShadow = "4px 4px 8px var(--shadow-dark), -4px -4px 8px var(--shadow-light)"
    })
  })

  // Add hover effects to cards
  const cards = document.querySelectorAll(".neu-card, .metric-card")
  cards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.classList.add("fade-in")
    })
  })
}

function addAnimations() {
  // Animate elements on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in")
      }
    })
  })

  const animatedElements = document.querySelectorAll(".neu-card, .metric-card")
  animatedElements.forEach((el) => observer.observe(el))
}

// Utility functions for API calls
async function fetchData(endpoint) {
  try {
    const response = await fetch(endpoint)
    return await response.json()
  } catch (error) {
    console.error("Error fetching data:", error)
    return null
  }
}

// Route optimization function
async function optimizeRoute(routeData) {
  try {
    const response = await fetch("/api/route-optimization", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(routeData),
    })
    return await response.json()
  } catch (error) {
    console.error("Error optimizing route:", error)
    return null
  }
}

async function getRouteAlternatives(routeData) {
  try {
    const response = await fetch("/api/route-alternatives", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(routeData),
    })
    return await response.json()
  } catch (error) {
    console.error("Error getting route alternatives:", error)
    return null
  }
}

async function getLiveTracking(routeId) {
  try {
    const response = await fetch(`/api/live-tracking/${routeId}`)
    return await response.json()
  } catch (error) {
    console.error("Error getting live tracking:", error)
    return null
  }
}

async function manageWaypoints(action, data) {
  try {
    const response = await fetch("/api/waypoints", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ action, ...data }),
    })
    return await response.json()
  } catch (error) {
    console.error("Error managing waypoints:", error)
    return null
  }
}

// Fuel price updates
async function updateFuelPrices() {
  const prices = await fetchData("/api/fuel-prices")
  if (prices) {
    // Update fuel price displays
    Object.keys(prices).forEach((fuelType) => {
      const element = document.getElementById(`price-${fuelType}`)
      if (element) {
        element.textContent = `R$ ${prices[fuelType].toFixed(2)}`
      }
    })
  }
}

// Export functions for use in other scripts
window.WiseRoutes = {
  fetchData,
  optimizeRoute,
  getRouteAlternatives,
  getLiveTracking,
  manageWaypoints,
  updateFuelPrices,
}
