# Dashboard AIFA - Pharma
# Autore: Carchedi Foca Marco
# Ultima modifica: 23 agosto 2025

library(shiny)
library(tidyverse)
library(readxl)
library(janitor)
library(shiny)
library(rsconnect)

df <- read_excel("consumo_farmaci.xlsx") %>%
  clean_names() %>%
  filter(if_all(everything(), ~ !is.na(.))) %>%
  distinct() %>%
  mutate(
    regione = str_to_title(regione),
    codice_atc = str_to_upper(atc1),
    spesa_totale = as.numeric(spesa_totale)
  )

ui <- fluidPage(
  titlePanel("Dashboard Consumo Farmaci AIFA"),
  sidebarLayout(
    sidebarPanel(
      selectInput("atc", "Classe ATC:", choices = unique(df$codice_atc)),
      sliderInput("anno", "Anno:", min = min(df$anno), max = max(df$anno), value = max(df$anno), step = 1)
    ),
    mainPanel(
      plotOutput("trendPlot"),
      tableOutput("summaryTable")
    )
  )
)

server <- function(input, output) {
  filtered_data <- reactive({
    df %>%
      filter(codice_atc == input$atc, anno <= input$anno)
  })

  output$trendPlot <- renderPlot({
    ggplot(filtered_data(), aes(x = anno, y = spesa_totale)) +
      geom_line() +
      geom_point() +
      labs(title = paste("Trend spesa per", input$atc), x = "Anno", y = "Spesa (€)") +
      theme_minimal()
  })

  output$summaryTable <- renderTable({
    filtered_data() %>%
      group_by(anno) %>%
      summarise(spesa = sum(spesa_totale, na.rm = TRUE))
  })
}

shinyApp(ui = ui, server = server)

