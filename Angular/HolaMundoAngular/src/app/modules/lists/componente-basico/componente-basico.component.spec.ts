import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponenteBasicoComponent } from './componente-basico.component';

describe('ComponenteBasicoComponent', () => {
  let component: ComponenteBasicoComponent;
  let fixture: ComponentFixture<ComponenteBasicoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComponenteBasicoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponenteBasicoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
