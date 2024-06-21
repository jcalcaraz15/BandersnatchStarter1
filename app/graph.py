from altair import Chart, Tooltip
from pandas import DataFrame
import altair as alt

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=alt.Color(target, scale=alt.Scale(scheme='dark2')),
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=300,
        height=500
    ).configure(
        background='rgba(0, 0, 0, 0.5)'  # Set the background color to black with 50% opacity
    ).configure_title(
        fontSize=20,
        color='white'  
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=16,
        labelColor='white',  
        titleColor='white'  
    ).configure_legend(
        titleFontSize=16,
        labelFontSize=14,
        titleColor='white',
        labelColor='white'  
    )

    return graph
