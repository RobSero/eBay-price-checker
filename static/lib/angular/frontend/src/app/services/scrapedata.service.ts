import { Injectable } from '@angular/core';
import {Observable} from 'rxjs'
import {HttpClient, HttpHeaders} from '@angular/common/http'

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type' : 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class ScrapedataService {
apiURL:string = 'http://localhost:5000/api/search/'


  constructor(private http:HttpClient) { }


// get data from api, requires search string argument
getEbayData(searchParam: string): Observable<any>{
  return this.http.get<any>(`${this.apiURL}${searchParam}`)
}


}
