import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="path",
    path="M 0,50 L 50,50 L 50,0",
    fillcolor="red",
    line=dict(color="red"),
    xref="x",
    yref="y"
)

fig.add_shape(
    type="path",
    path="M 0,0 L 0,50 L 50,50",
    fillcolor="red",
    line=dict(color="red"),
    xref="x",
    yref="y"
)

fig.add_shape(
    type="path",
    path="M 100,50 L 50,50 L 50,100",
    fillcolor="red",
    line=dict(color="red"),
    xref="x",
    yref="y"
)

fig.add_shape(
    type="path",
    path="M 100,100 L 100,50 L 50,50",
    fillcolor="red",
    line=dict(color="red"),
    xref="x",
    yref="y"
)

fig.update_layout(
    xaxis=dict(
        range=[0, 100],
        showticklabels=False,
        showgrid=False,
        zeroline=False
    ),
    yaxis=dict(
        range=[0, 100],
        showticklabels=False,
        showgrid=False,
        zeroline=False
    ),
    showlegend=False,
    width=400,
    height=400,
    margin=dict(
        l=20,
        r=20,
        b=20,
        t=20
    ),
)

fig.show()
