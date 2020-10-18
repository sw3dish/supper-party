import * as Rx from "rxjs";
import { throttleTime, mergeMap, map, startWith } from "rxjs/operators";

const endpoint = "http://localhost:4000";
const query = `
{
  recipes {
    title
    url
    description
  }
}
`;

const refreshButton = document.getElementById("refresh");
const recipe1 = document.getElementById("recipe_1");

const refreshClickStream$ = Rx.fromEvent(refreshButton, "click");

const requestStream$ = refreshClickStream$.pipe(
  startWith("start"),
  throttleTime(1000),
  map(() => endpoint)
);

const responseStream$ = requestStream$.pipe(
  mergeMap((requestUrl) =>
    Rx.from(
      fetch(requestUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({ query }),
      })
        .then((response) => response.json())
        .then((data) => data.data.recipes)
    )
  )
);

const recipe1Stream$ = Rx.merge(
  responseStream$.pipe(map((recipes) => recipes[0])),
  refreshClickStream$.pipe(map(() => null))
).pipe(startWith(null));

recipe1Stream$.subscribe((recipe) => {
  if (recipe === null) {
    recipe1.innerText = "";
  } else {
    recipe1.innerText = recipe.title;
  }
});
