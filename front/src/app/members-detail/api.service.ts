import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root',
})
export class ApiService {
  baseUrl = 'http://localhost:8000/';
  token = 'Token 2f83c7f763f9ec06a3aa05f52d901af2f00d9c5f';
  httpHeaders = new HttpHeaders()
    .set(
      // 'Content-Type',
      // 'applications/json'
      'X-CSRFToken',
      'csrftoken'
    )
    .set('Authorization', this.token);

  //  interação com a api
  constructor(private http: HttpClient) {}

  getMember(id: any): Observable<any> {
    return this.http.get(this.baseUrl + 'menbers/' + id + '/', {
      headers: this.httpHeaders,
    });
  }
  // put atualizar o dado
  updateMember(menber: any): Observable<any> {
    let body = {
      name: menber.name,
      surname: menber.surname,
      email: menber.email,
      phone: menber.phone,
      d_nasc: menber.d_nasc,
      andress: menber.andress,
      senha: menber.senha,

      // photo: menber.photo,
    };

    return this.http.put(this.baseUrl + 'menbers/' + menber.id + '/', body, {
      headers: this.httpHeaders,
    });
  }
  // deletar membro
  deleteMember(id: any): Observable<any> {
    return this.http.delete(this.baseUrl + 'menbers/' + id + '/', {
      headers: this.httpHeaders,
    });
  }
}
