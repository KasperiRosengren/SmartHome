import React from 'react';
import LineChartTest from './LineChartTest';




export default class RealZone extends React.Component {
    render() {
      return (
        <div className="zone">
                <div className="zoneTitle">{this.props.dataTo.zone}</div>
                <div className="outlets">
                    <div className="outlet"><button type="button">ON</button></div>
                    <div className="outlet"><button type="button">ON</button></div>
                    <div className="outlet"><button type="button">ON</button></div>
                    <div className="outlet"><button type="button">ON</button></div>
                </div>
                <div className="graph"><LineChartTest /></div>
                <div className="leds">
                    <div className="info">
                        <div className="ledName">Ceiling Strip</div>
                        <div className="patterns">
                            <div className="pattern">pattern 1</div>
                            <div className="pattern">pattern 2</div>
                            <div className="pattern">pattern 3</div>
                        </div>
                    </div>
                    <div className="colorpicker">Color Wheel!</div>
                </div>
            </div>
      );
    }
  }