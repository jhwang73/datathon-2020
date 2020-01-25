import React from "react";

import { VictoryBar } from "victory";

const styles = {
  container: {
    backgroundColor: "#ccc",
    borderRadius: 3,
    width: 500,
    height: 500,
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

const BarChart = () => {
  return (
    <div style={styles.container}>
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
    
export default BarChart;