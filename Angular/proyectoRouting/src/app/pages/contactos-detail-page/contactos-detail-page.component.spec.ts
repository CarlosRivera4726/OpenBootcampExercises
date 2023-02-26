import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContactosDetailPageComponent } from './contactos-detail-page.component';

describe('ContactosDetailPageComponent', () => {
  let component: ContactosDetailPageComponent;
  let fixture: ComponentFixture<ContactosDetailPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ContactosDetailPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ContactosDetailPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
