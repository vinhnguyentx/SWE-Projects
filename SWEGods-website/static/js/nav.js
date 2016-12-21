var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
                    "Orange": "#FF9900",
                    "Greek": "#e25822",
                    "Black": "#000000",
};


function Application() {
  return (



    <nav className="navbar navbar-inverse navbar-fixed-top" role="navigation" style={{backgroundColor: bgColors.Yellow}}>
        <div className="container">
            <div className="navbar-header">
                <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span className="sr-only">Toggle navigation</span>
                    <span className="icon-bar"></span>
                    <span className="icon-bar"></span>
                    <span className="icon-bar"></span>
                </button>
                <a className="navbar-brand" href="/" style={{color: bgColors.Yellow}}>Greek Mythology</a>
            </div>
            <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul className="nav navbar-nav">
                    <li>
                        <a href="/static/gods.html" style={{color: bgColors.Yellow}}>Gods</a>
                    </li>
                    <li>
                        <a href="/static/heroes.html" style={{color: bgColors.Yellow}}>Heroes</a>
                    </li>
                    <li>
                        <a href="/static/locations.html" style={{color: bgColors.Yellow}}>Locations</a>
                    </li>
                    <li>
                        <a href="/static/myths.html" style={{color: bgColors.Yellow}}>Myths</a>
                    </li>
                    <li>
                        <a href="/static/about.html" style={{color: bgColors.Yellow}}>About</a>
                    </li>
                </ul>

                <form className="navbar-form navbar-left" role="search" action="/search" method="get">
                  <div className="form-group">
                    <input name="query" id="searchval" type="text" className="form-control" placeholder="Search"></input>
                  </div>
                  <button type="submit" className="btn btn-default">Submit</button>
                </form>
                
            </div>
        </div>
    </nav>
  );
}

ReactDOM.render(<Application/>, document.getElementById('nav'));
