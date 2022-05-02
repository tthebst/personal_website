use yew::prelude::*;
use yew_router::prelude::*;

// ===================================================================================
// for {username}.github.io

#[derive(Clone, Routable, PartialEq)]
enum RootRoute {
    #[at("/")]
    Home,
    #[at("/about")]
    About,
    #[not_found]
    #[at("/404")]
    NotFound,
}

fn root_route(routes: &RootRoute) -> Html {
    match routes {
        RootRoute::Home => html! { <p class="text-4xl">{ "WIP" }</p> },
        RootRoute::About => html! { <p>{ "About" }</p> },
        RootRoute::NotFound => html! { <p>{ "Not Found" }</p> },
    }
}

// ===================================================================================

/// main root
#[function_component(App)]
fn app() -> Html {
    html! {
        // ********************************************************
        // **    basename is not supported on yew 0.19.0 yet.    **
        // <BrowserRouter basename="/yew-template-for-github-io/">
        //     <Switch<Route> render={Switch::render(switch)} />
        // </BrowserRouter>
        // ********************************************************
        <BrowserRouter>
            <Switch<RootRoute> render={Switch::render(root_route)} />
        </BrowserRouter>
    }
}

/// entry point
fn main() {
    yew::start_app::<App>();
}
