import React, { Component } from "react";
import { render } from "react-dom";
import { VictoryBar } from "victory";

const styles = {
  container: {
    backgroundColor: "#ccc",
    borderRadius: 3,
    width: 100,
    height: 100,
    padding: 4,
    margin: 8
  },
}

const sampleData = [
  { x: 1, y: 2, y0: 1 },
  { x: 2, y: 3, y0: 2 },
  { x: 3, y: 5, y0: 2 },
  { x: 4, y: 4, y0: 3 },
  { x: 5, y: 6, y0: 3 }
];

class BarChart extends Component {
  render() {
    return (
      <div styles={styles.container}>
        <h3>Click Me</h3>
        <VictoryBar
          animate={{
            duration: 2000,
            onLoad: { duration: 1000 }
          }}
          style={{
            data: { fill: "#c43a31" }
          }}
          events={[{
            target: "data",
            eventHandlers: {
              onClick: () => {
                return [
                  {
                    target: "data",
                    mutation: (props) => {
                      const fill = props.style && props.style.fill;
                      return fill === "black" ? null : { style: { fill: "black" } };
                    }
                  }
                ];
              }
            }
          }]}
          data={sampleData}
        />
      </div>
    );
  }
}

export default BarChart;